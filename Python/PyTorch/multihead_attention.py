import math
import torch
from torch import nn, einsum
import torch.nn.functional as F

from einops import rearrange, repeat
from einops.layers.torch import Rearrange



class Attention(nn.Module):
    def __init__(self, dim, heads = 8, dim_head = 64, dropout = 0., project_out=False):
        super().__init__()
        inner_dim = dim_head *  heads

        self.heads = heads
        self.scale = dim_head ** -0.5

        self.attend = nn.Softmax(dim = -1)
        self.to_qkv = nn.Linear(dim, inner_dim * 3, bias = False)

        self.to_out = nn.Sequential(
            nn.Linear(inner_dim, dim),
            nn.Dropout(dropout)
        ) if project_out else nn.Identity()

    def forward(self, x, attn_bias=None):
        b, n, _, h = *x.shape, self.heads
        qkv = self.to_qkv(x).chunk(3, dim = -1)
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> b h n d', h = h), qkv)
        dots = einsum('b h i d, b h j d -> b h i j', q, k) * self.scale
        if attn_bias is not None:
            assert attn_bias.shape==dots.shape, "wrong shape: attn_bias: {} recieved, {} expected".format(tuple(attn_bias.shape),tuple(dots.shape))
            dots=dots+attn_bias
        attn = self.attend(dots)

        out = einsum('b h i j, b h j d -> b h i d', attn, v)
        out = rearrange(out, 'b h n d -> b n (h d)')
        return self.to_out(out),attn


if __name__=="__main__":
    SEED=0
    torch.manual_seed(SEED)
    torch.cuda.manual_seed(SEED)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    
    config={
        'dim':1024,
        'heads':8,
        'dim_head':128
    }
    inp=torch.rand(2,30,1024)
    inp_rearranged=rearrange(inp,'b n d -> n b d')
    multihead_attn = nn.MultiheadAttention(embed_dim=config["dim"], num_heads=config["heads"], bias=False)
    # attn_output, attn_output_weights = multihead_attn(query, key, value)
    print("nn.MultiheadAttention")
    for k,v in multihead_attn.named_parameters():
        print(k)
        print(v.shape)
    res,attn=multihead_attn(inp_rearranged,inp_rearranged,inp_rearranged)
    print(attn)

    multihead_attn2 = Attention(
        dim=config['dim'],
        heads=config['heads'],
        dim_head=config['dim_head'],
        project_out=True
    )
    multihead_attn2.to_qkv.weight.data[:]=multihead_attn.in_proj_weight
    multihead_attn2.to_out[0].weight.data[:]=multihead_attn.out_proj.weight
    multihead_attn2.to_out[0].bias.data[:]=multihead_attn.out_proj.bias

    print("Attention")
    for k,v in multihead_attn2.named_parameters():
        print(k)
        print(v.shape)
    res,attn=multihead_attn2(inp)
    # print(rearrange(res,'b n d -> n b d'))
    print(attn.mean(axis=1))
