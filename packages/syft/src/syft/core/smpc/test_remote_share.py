# third party
import numpy as np

# syft absolute
import syft as sy
from syft.core.tensor.share_tensor import ShareTensor
from syft.core.tensor.passthrough import PassthroughTensor
from syft.core.tensor.tensor import Tensor

alice = sy.VirtualMachine(name="alice")
bob = sy.VirtualMachine(name="bob")


alice_client = alice.get_client()
bob_client = bob.get_client()

orig_tensor = Tensor(np.array([[1, 2, 3], [4, 5, 6]]))
shape = orig_tensor.shape

remote_tensor = orig_tensor.send(alice_client)

import pdb

pdb.set_trace()
remote_tensor.share(alice, bob)