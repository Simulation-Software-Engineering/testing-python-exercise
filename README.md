# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

### unittest log

python3 -m pytest tests/unit/test_diffusion2d_functions.py 
===================================================================================== test session starts ======================================================================================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/kim/Dokumente/Uni/SSE/Exercises/testing-python-exercise
collected 3 items                                                                                                                                                                              

tests/unit/test_diffusion2d_functions.py FFF                                                                                                                                             [100%]

=========================================================================================== FAILURES ===========================================================================================
____________________________________________________________________________________ test_initialize_domain ____________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # set values
        w  = 2.
        h  = 3.
        dx = 0.5
        dy = 0.5
    
        nx_expected = 4
        ny_expected = 6
    
        solver = SolveDiffusion2D()
        solver.initialize_domain(w, h, dx, dy)
    
>       assert nx_expected == solver.ny
E       assert 4 == 6
E        +  where 6 = <diffusion2d.SolveDiffusion2D object at 0x7f46619c42e0>.ny

tests/unit/test_diffusion2d_functions.py:24: AssertionError
_____________________________________________________________________________ test_initialize_physical_parameters ______________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        T_cold = 100.
        T_hot  = 1000.
    
        d      = 2.
        dx     = 1.
        dy     = 1.
    
        dt_expected = 0.125
    
        solver.dx = dx
        solver.dy = dy
    
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        assert dt_expected == solver.dt
>       assert T_cold == solver.T_hot
E       assert 100.0 == 1000.0
E        +  where 1000.0 = <diffusion2d.SolveDiffusion2D object at 0x7f4661922df0>.T_hot

tests/unit/test_diffusion2d_functions.py:49: AssertionError
------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------
dt = 0.125
__________________________________________________________________________________ test_set_initial_condition __________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        solver.T_hot  = 333.
        solver.T_cold = -17.
        solver.nx     = 2
        solver.ny     = 2
        solver.dx     = 4.5
        solver.dy     = 5.5
    
        u_expected = np.array([[333., -17.], [-17., 333.]])
        u_returned  = solver.set_initial_condition()
    
        #assert all([a == b for a, b in zip(u_expected, u_returned)])
>       assert u_expected[0][0] == u_returned[0][0]
E       assert 333.0 == -17.0

tests/unit/test_diffusion2d_functions.py:70: AssertionError
=================================================================================== short test summary info ====================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 4 == 6
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 100.0 == 1000.0
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 333.0 == -17.0
====================================================================================== 3 failed in 0.24s =======================================================================================

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
