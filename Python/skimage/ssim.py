img = img_as_float(data.camera())
rows, cols = img.shape

noise = np.ones_like(img) * 0.2 * (img.max() - img.min())
rng = np.random.default_rng()
noise[rng.random(size=noise.shape) > 0.5] *= -1

noise_right_half=noise.copy()
noise_right_half[:,:noise_right_half.shape[1]//2]=0
noise_right_half=np.abs(noise_right_half)

noise2=noise.copy()
noise2[:,noise2.shape[1]//2:]*=0.3
noise2=np.abs(noise2)

img_noise = np.clip(img + noise, 0, 1)
img_const = np.clip(img + abs(noise), 0, 1)
img_rev = np.clip(img + noise2, 0, 1)
img_right_half = np.clip(img + noise_right_half, 0, 1)

fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(12.5, 8), sharex=True, sharey=True)
ax = axes

mse_none = mean_squared_error(img, img)
ssim_none, S_none = ssim(img, img, data_range=img.max() - img.min(), full=True)

mse_noise = mean_squared_error(img, img_noise)
ssim_noise, S_noise = ssim(img, img_noise, data_range=img_noise.max() - img_noise.min(), full=True)

mse_const = mean_squared_error(img, img_const)
ssim_const, S_const = ssim(img, img_const, data_range=img_const.max() - img_const.min(), full=True)

mse_half = mean_squared_error(img, img_right_half)
ssim_half, S_half = ssim(img, img_right_half, data_range=img_right_half.max()-img_right_half.min(), full=True)

mse_rev = mean_squared_error(img, img_rev)
ssim_rev, S_rev = ssim(img, img_rev, data_range=img_rev.max()-img_rev.min(), full=True)

ax[0,0].imshow(img, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0,0].set_xlabel(f'MSE: {mse_none:.2f}, SSIM: {ssim_none:.2f}')
ax[0,0].set_title('Original image')
ax[1,0].imshow(S_none, cmap=plt.cm.gray, vmin=S_none.min(), vmax=S_none.max())

ax[0,1].imshow(img_noise, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0,1].set_xlabel(f'MSE: {mse_noise:.2f}, SSIM: {ssim_noise:.2f}')
ax[0,1].set_title('Image with noise')
ax[1,1].imshow(S_noise, cmap=plt.cm.gray, vmin=S_noise.min(), vmax=S_noise.max())

ax[0,2].imshow(img_const, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0,2].set_xlabel(f'MSE: {mse_const:.2f}, SSIM: {ssim_const:.2f}')
ax[0,2].set_title('Image plus constant')
ax[1,2].imshow(S_const, cmap=plt.cm.gray, vmin=S_noise.min(), vmax=S_noise.max())


ax[0,3].imshow(img_right_half, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0,3].set_xlabel(f'MSE: {mse_rev:.2f}, SSIM: {ssim_rev:.2f}')
ax[0,3].set_title('Image right half')
ax[1,3].imshow(S_half, cmap=plt.cm.gray, vmin=S_half.min(), vmax=S_half.max())

ax[0,4].imshow(img_rev, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0,4].set_xlabel(f'MSE: {mse_rev:.2f}, SSIM: {ssim_rev:.2f}')
ax[0,4].set_title('Image reversed')
ax[1,4].imshow(S_rev, cmap=plt.cm.gray, vmin=S_noise.min(), vmax=S_noise.max())

plt.tight_layout()
plt.show()