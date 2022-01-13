# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
================================== FAILURES ===================================
___________________________ test_initialize_domain ____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        w = 12.
        h = 20.
        dx = 0.4
        dy = 0.2
        expected_nx = 30 #int(w / dx)
        expected_ny = 100 #int(h / dy)
    
        solver.initialize_domain(w,h,dx,dy)
    
>       assert solver.nx == expected_nx
E       assert 50 == 30
E        +  where 50 = <diffusion2d.SolveDiffusion2D object at 0x10d149970>.nx

tests/unit/test_diffusion2d_functions.py:24: AssertionError
_____________________ test_initialize_physical_parameters _____________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 0.2
        solver.dy = 0.4
        d=5.
    
        #dx**2 * dy**2 / (2 * d * (dx**2 + dy**2))
        expected_dt = pytest.approx(0.0032, abs=0.000001)
    
        solver.initialize_physical_parameters(d)
    
>       assert solver.dt == expected_dt
E       assert 0.008000000000000002 == 0.0032 ± 1.0e-06
E        +  where 0.008000000000000002 = <diffusion2d.SolveDiffusion2D object at 0x10d0e8520>.dt

tests/unit/test_diffusion2d_functions.py:41: AssertionError
---------------------------- Captured stdout call -----------------------------
dt = 0.008000000000000002
_________________________ test_get_initial_condition __________________________

    def test_get_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.T_cold = 300.
        solver.T_hot = 700.
        solver.dx = 0.1
        solver.dy = 0.2
        solver.nx = 100
        solver.ny = 50
    
        expected_u = solver.T_cold * np.ones((solver.nx, solver.ny))
    
        # Initial conditions - circle of radius r centred at (cx,cy) (mm)
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(solver.nx):
            for j in range(solver.ny):
                p2 = (i * solver.dx - cx) ** 2 + (j * solver.dx - cy) ** 2
                #p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy‚ - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = solver.T_hot
    
        actual_u = solver.get_initial_condition()
    
>       assert np.all(actual_u == expected_u)
E       assert False
E        +  where False = <function all at 0x1098d85e0>(array([[300.,... 300., 300.]]) == array([[300.,... 300., 300.]])
E        +    where <function all at 0x1098d85e0> = np.all
E           Use -v to get the full diff)

tests/unit/test_diffusion2d_functions.py:69: AssertionError
=========================== short test summary info ===========================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - as...
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters
FAILED tests/unit/test_diffusion2d_functions.py::test_get_initial_condition
========================= 3 failed, 2 passed in 0.66s =========================
### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
