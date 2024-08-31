## FedNTD Paper

Federated Learning approaches enable the learning of a global model while preserving client's data privacy. In Federated leraning, clients independently train local models using their private data and the server aggregates them into a single global model. 

This approach often struggles with performance due to data hetergeneity across clients. The FedNTD method addresses this problem by refining the distillation process and improving generalization.

While the server aggregates local models, the distribution where they are trained is largely different from those of previous rounds resulting in *forgetting*. The global model struggles to preserve previous knowledge.

They observed that during each communication round although the global models accuracy on classes with a higher proportion of scamples in the local dataset increased, it's accuracy on out-local distribution of data decreased compared to its previous iteration.

To help prevent forgetting and improve accuracy on out-local distribution of data, the paper proposes "Not-True-Distillation". This method modifies the loss function in each epoch to take into account the Kullback-Leibler Divergence loss between the refined logits of the local and global models.

What are refined logits and how is this done?

For each batch of data, we remove the logits (output) for the "true class" or the actual label of the data for both the global model and local model and call them refined logits. We then calculate the KL Divergence betwen the refined logits of the local and global models and multiplies them with a hyperparameter (Beta) that represents the strength of knowledge preservation on the out-local distribution.

We then add this loss to the normal loss function (in this case cross entropy loss) of the local model using the unrefined logits.

In this new loss function, taking into account Not-True-Distillation: we attain knowledge on the in-local distribution by following the true-class signals from the labeled data in local datasets and also preserve the previous konwledge on the out-local distribution by following the global model's perspective coreesponding to the not-true class signals.

On comparison with other strategies such as FedAvg, the paper shows that although there is little change in local accuracy on in-local distribution, FedNTD significanly improves the local accuracy on out-local distribution, which implies it prevents forgetting. 
Along with this, the test accuracy of the global model also improves substantially. This gap is enlarged as the number of local epochs increase.
