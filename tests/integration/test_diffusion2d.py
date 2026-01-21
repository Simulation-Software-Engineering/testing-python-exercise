"""
Tests for functionality checks in class SolveDiffusion2D
"""
import numpy as np
import pytest

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Integration test:
    initialize_domain + initialize_physical_parameters
    检查 dt 是否按公式正确计算
    """
    solver = SolveDiffusion2D()

    # 先初始化计算域
    w, h = 3.0, 2.0
    dx, dy = 0.5, 0.25
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

    # 再初始化物理参数
    d = 4.0
    T_cold = 300.0
    T_hot = 700.0
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

    # 手算 dt
    dx2, dy2 = dx * dx, dy * dy
    expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))

    assert np.isclose(solver.dt, expected_dt)


def test_set_initial_condition():
    """
    Integration test:
    initialize_domain + initialize_physical_parameters + set_initial_condition
    检查整个初始温度场 u 是否正确
    """
    solver = SolveDiffusion2D()

    # 完整工作流
    w, h = 3.0, 2.0
    dx, dy = 0.5, 0.25
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=4.0, T_cold=300.0, T_hot=700.0)

    u0 = solver.set_initial_condition()

    # 构造 expected_u（和源码逻辑完全一致）
    expected_u = solver.T_cold * np.ones((solver.nx, solver.ny), dtype=float)

    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = solver.T_hot

    assert np.allclose(u0, expected_u)

