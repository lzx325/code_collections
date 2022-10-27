def plot(label,pred):
    precision, recall, _ =precision_recall_curve(label,pred)
    fpr,tpr,_=roc_curve(label,pred)
    auc_pr=auc(recall,precision)
    auc_roc=auc(fpr,tpr)
    plt.plot(recall,precision,label="PR")
    plt.plot(fpr,tpr,label="ROC")
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])
    plt.title(f"AUCPR={auc_pr:.4f},AUCROC={auc_roc:.4f}")
    plt.legend()

label=np.array([1.]*900+[0.]*100)
# random classification
pred1=np.random.rand(1000)
plot(label,pred1)
plt.figure()
# same prediction
pred2=np.full((1000,),1.0)
plot(label,pred2)
# perfect misclassification
plt.figure()
pred3=np.linspace(0,1,1000)
plot(label,pred3)