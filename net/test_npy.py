import numpy as np  

#导入npy文件路径位置
psnr = np.load('/home/louanqi/pycharmp/FFA-Net/net/numpy_files/rshaze_train_ffa_3_19_500000_psnrs.npy')
ssim = np.load('/home/louanqi/pycharmp/FFA-Net/net/numpy_files/rshaze_train_ffa_3_19_500000_ssims.npy')

print(max(psnr))
print(max(ssim))
