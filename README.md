# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/sabri/UNI/Sem4/SimulationSoftwareEngineering/git-repos/SSE_Exercises/testing-python-exercise
collected 5 items                                                              

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                             [100%]

=================================== FAILURES ===================================
____________________________ test_initialize_domain ____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        # Expected
        # w = 12.
        # h = 15.
        # dx = 0.2
        # dy = 0.15
        expected_nx = 60
        expected_ny = 100
    
        # Actual
        solver.initialize_domain(w=12., h=15., dx=0.2, dy=0.15)
    
        actual_nx = solver.nx
        actual_ny = solver.ny
    
        #Test
>       assert actual_nx == expected_nx
E       assert 75 == 60

tests/unit/test_diffusion2d_functions.py:29: AssertionError
_____________________ test_initialize_physical_parameters ______________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        # Expected
        expected_T_cold = 250
        expected_T_hot = 650
        #expected_dt = 0.0009
        expected_dt = 0.0009000000000000002
    
        # Actual
        solver.dx = 0.2
        solver.dy = 0.15
        solver.initialize_physical_parameters(d=8., T_cold=expected_T_cold, T_hot=expected_T_hot)
        actual_T_cold = solver.T_cold
        actual_T_hot = solver.T_hot
        actual_dt = solver.dt
    
        # Test
        assert expected_T_cold == actual_T_cold
        assert expected_T_hot == actual_T_hot
>       assert expected_dt == actual_dt
E       assert 0.0009000000000000002 == 0.09000000000000002

tests/unit/test_diffusion2d_functions.py:55: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.09000000000000002
__________________________ test_set_initial_condition __________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        
        # Paramters
        T_cold = 250
        T_hot = 650
        nx = 50
        ny = 70
        dx = 0.2
        dy = 0.15
        
        # Expected  
        expected_u = T_cold * np.ones((nx, ny))
    
        # Initial conditions - circle of radius r centred at (cx,cy) (mm)
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = T_hot
    
        # Actual
        solver.T_cold = T_cold
        solver.T_hot = T_hot
        solver.nx = nx
        solver.ny = ny
        solver.dx = dx
        solver.dy = dy
        actual_u = solver.set_initial_condition()
    
>       np.testing.assert_array_equal(actual_u, expected_u)
E       AssertionError: 
E       Arrays are not equal
E       
E       Mismatched elements: 414 / 3500 (11.8%)
E       Max absolute difference: 1.
E       Max relative difference: 0.00153846
E        x: array([[250., 250., 250., ..., 250., 250., 250.],
E              [250., 250., 250., ..., 250., 250., 250.],
E              [250., 250., 250., ..., 250., 250., 250.],...
E        y: array([[250., 250., 250., ..., 250., 250., 250.],
E              [250., 250., 250., ..., 250., 250., 250.],
E              [250., 250., 250., ..., 250., 250., 250.],...

tests/unit/test_diffusion2d_functions.py:92: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - ass...
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition
```

### unittest log

```
Fdt = 0.09000000000000002
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sabri/UNI/Sem4/SimulationSoftwareEngineering/git-repos/SSE_Exercises/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 47, in test_initialize_domain
    self.assertEqual(actual_nx,expected_nx)
AssertionError: 75 != 60

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sabri/UNI/Sem4/SimulationSoftwareEngineering/git-repos/SSE_Exercises/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 73, in test_initialize_physical_parameters
    self.assertEqual(expected_dt, actual_dt)
AssertionError: 0.0009000000000000002 != 0.09000000000000002

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sabri/UNI/Sem4/SimulationSoftwareEngineering/git-repos/SSE_Exercises/testing-python-exercise/tests/unit/test_diffusion2d_functions.py", line 111, in test_set_initial_condition
    self.assertTrue((actual_u == expected_u).all())
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=3)
```

### integration test log
```
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/sabri/UNI/Sem4/SimulationSoftwareEngineering/git-repos/SSE_Exercises/testing-python-exercise
collected 2 items                                                                                                                                                                                                 

tests/integration/test_diffusion2d.py FF                                                                                                                                                                    [100%]

==================================================================================================== FAILURES =====================================================================================================
_______________________________________________________________________________________ test_initialize_physical_parameters _______________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain()
        solver.initialize_physical_parameters()
    
        # Expected
        expected_dt = pytest.approx(0.000625)
    
        # Actual
        actual_dt = solver.dt
    
        # Test
>       assert expected_dt == actual_dt
E       assert 0.000625 ± 6.3e-10 == 0.06250000000000001

tests/integration/test_diffusion2d.py:24: AssertionError
---------------------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------------------
dt = 0.06250000000000001
___________________________________________________________________________________________ test_set_initial_condition ____________________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        # Paramters
        T_cold = 250
        T_hot = 650
        nx = 50
        ny = 70
        dx = 0.2
        dy = 0.15
    
        # Expected
        expected_u = T_cold * np.ones((nx, ny))
    
        # Initial conditions - circle of radius r centred at (cx,cy) (mm)
        r, cx, cy = 2, 5, 5
        r2 = r ** 2
        for i in range(nx):
            for j in range(ny):
                p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
                if p2 < r2:
                    expected_u[i, j] = T_hot
    
        # Actual
        solver.T_cold = T_cold
        solver.T_hot = T_hot
        solver.nx = nx
        solver.ny = ny
        solver.dx = dx
        solver.dy = dy
        actual_u = solver.set_initial_condition()
    
        # Test
>       assert ((actual_u == expected_u).all())
E       assert False
E        +  where False = <built-in method all of numpy.ndarray object at 0x7fdcd2def0f0>()
E        +    where <built-in method all of numpy.ndarray object at 0x7fdcd2def0f0> = array([[250.,... 250., 250.]]) == array([[250.,... 250., 250.]])
E             Use -v to get the full diff.all

tests/integration/test_diffusion2d.py:62: AssertionError
============================================================================================= short test summary info =============================================================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.000625 ± 6.3e-10 == 0.06250000000000001
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert False
```


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
