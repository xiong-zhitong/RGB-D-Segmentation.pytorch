import torch
import torch.autograd.gradcheck as gradcheck
from deform_conv import DeformConvPack
from modulated_deform_conv import ModulatedDeformConvPack



conv = DeformConvPack(1,1,3,1,1).cuda()
deformconv = ModulatedDeformConvPack(1,1,3,1,1).cuda()
inp = torch.randn([1,1,3,3]).cuda()
inp.requires_grad = True
print(conv)

#test = gradcheck(conv, (inp), eps=1e-6, atol=1e-4, raise_exception=True)
test2 = gradcheck(deformconv, (inp), eps=1e-6, atol=1e-4, raise_exception=True)
print(test2)
