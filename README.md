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
E        +  where 50 = <diffusion2d.SolveDiffusion2D object at 0x10af5f520>.nx

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
E        +  where 0.008000000000000002 = <diffusion2d.SolveDiffusion2D object at 0x10afd8c70>.dt

tests/unit/test_diffusion2d_functions.py:41: AssertionError
---------------------------- Captured stdout call -----------------------------
dt = 0.008000000000000002
=========================== short test summary info ===========================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - as...
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters
========================= 2 failed, 3 passed in 0.50s =========================
### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
