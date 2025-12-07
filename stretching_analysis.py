import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 读取力数据（当前只有力，假设距离是时间对应的递增序列，或用时间代替距离）
data = np.loadtxt('smd_pullf.xvg', comments=['#', '@'])
time = data[:, 0]
force = data[:, 1]
force_nN = force * 1.66054

# 绘制力-时间曲线（替代力-距离，若有pullx.xvg可替换）
plt.figure(figsize=(10, 6))
plt.plot(time, force_nN, color='#2E86AB', linewidth=2)
plt.xlabel('Time (ps)', fontsize=12)
plt.ylabel('Stretching Force (nN)', fontsize=12)
plt.title('Protein Stretching Force-Time Curve', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.savefig('stretching_force_curve.png', dpi=300, bbox_inches='tight')
plt.show()

max_force = np.max(force_nN)
avg_force = np.mean(force_nN)
print("=== 拉伸强度分析 ===")
print(f"最大拉伸强度: {max_force:.2f} nN")
print(f"平均拉伸强度: {avg_force:.2f} nN")
