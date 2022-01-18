# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

> python -m pytest
================================================ test session starts =================================================
platform linux -- Python 3.8.11, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/hornekte/Desktop/testing-python-exercise
collected 5 items                                                                                                    

tests/integration/test_diffusion2d.py ..                                                                       [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                   [100%]

====================================================== FAILURES ======================================================
_______________________________________________ test_initialize_domain _______________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w = 20.0
        h = 40.0
        dx = 0.2
        dy = 0.2
        solver.initialize_domain(w, h, dx, dy)
    
        expected_nx = 100
        expected_ny = 200
    
        actual_nx = solver.nx
        actual_ny = solver.ny
    
>       assert actual_nx == expected_nx
E       assert 200 == 100

tests/unit/test_diffusion2d_functions.py:28: AssertionError
________________________________________ test_initialize_physical_parameters _________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        d = 5.0
        T_cold = 200.0
        T_hot = 800.0
        solver.dx = 0.2
        solver.dy = 0.4
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        expected_dt = approx(0.0032, abs=0.0001)
    
        actual_dt = solver.dt
    
>       assert actual_dt == expected_dt
E       assert 0.0008000000000000001 == 0.0032 ± 1.0e-04

tests/unit/test_diffusion2d_functions.py:48: AssertionError
------------------------------------------------ Captured stdout call ------------------------------------------------
dt = 0.0008000000000000001
_____________________________________________ test_set_initial_condition _____________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.T_cold = 200.0
        solver.T_hot = 800.0
        solver.nx = 5
        solver.ny = 10
        solver.dx = 1.0
        solver.dy = 2.0
    
        expected_u = np.ones((5,10))*200.
        expected_u[4,2:4]=800.
    
        actual_u = solver.set_initial_condition()
    
        print(actual_u)
    
>       np.testing.assert_allclose(actual_u,expected_u)
E       AssertionError: 
E       Not equal to tolerance rtol=1e-07, atol=0
E       
E       Mismatched elements: 2 / 50 (4%)
E       Max absolute difference: 600.
E       Max relative difference: 0.75
E        x: array([[200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],
E              [200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],
E              [200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],...
E        y: array([[200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],
E              [200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],
E              [200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],...

tests/unit/test_diffusion2d_functions.py:70: AssertionError
------------------------------------------------ Captured stdout call ------------------------------------------------
[[200. 200. 200. 200. 200. 200. 200. 200. 200. 200.]
 [200. 200. 200. 200. 200. 200. 200. 200. 200. 200.]
 [200. 200. 200. 200. 200. 200. 200. 200. 200. 200.]
 [200. 200. 200. 200. 200. 200. 200. 200. 200. 200.]
 [200. 200. 200. 200. 200. 200. 200. 200. 200. 200.]]
============================================== short test summary info ===============================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 200 == 100
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.0008000000000000001...
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - AssertionError: 
============================================ 3 failed, 2 passed in 0.86s =============================================


### unittest log


> python -m pytest
================================================ test session starts =================================================
platform linux -- Python 3.8.11, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/hornekte/Desktop/testing-python-exercise
collected 5 items                                                                                                    

tests/integration/test_diffusion2d.py ..                                                                       [ 40%]
tests/unit/test_diffusion2d_functions.py FFF                                                                   [100%]

====================================================== FAILURES ======================================================
_______________________________________ TestOperations.test_initialize_domain ________________________________________

self = <test_diffusion2d_functions.TestOperations testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 20.0
        h = 40.0
        dx = 0.2
        dy = 0.2
        self.solver.initialize_domain(w, h, dx, dy)
    
        expected_nx = 100
        expected_ny = 200
    
        actual_nx = self.solver.nx
        actual_ny = self.solver.ny
    
>       self.assertEqual(actual_nx, expected_nx)
E       AssertionError: 200 != 100

tests/unit/test_diffusion2d_functions.py:32: AssertionError
_________________________________ TestOperations.test_initialize_physical_parameters _________________________________

self = <test_diffusion2d_functions.TestOperations testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        d = 5.0
        T_cold = 200.0
        T_hot = 800.0
        self.solver.dx = 0.2
        self.solver.dy = 0.4
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        expected_dt = 0.0032
    
        actual_dt = self.solver.dt
    
>       self.assertAlmostEqual(actual_dt,expected_dt)
E       AssertionError: 0.0008000000000000001 != 0.0032 within 7 places (0.0024000000000000002 difference)

tests/unit/test_diffusion2d_functions.py:51: AssertionError
------------------------------------------------ Captured stdout call ------------------------------------------------
dt = 0.0008000000000000001
_____________________________________ TestOperations.test_set_initial_condition ______________________________________

self = <test_diffusion2d_functions.TestOperations testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.T_cold = 200.0
        self.solver.T_hot = 800.0
        self.solver.nx = 5
        self.solver.ny = 10
        self.solver.dx = 1.0
        self.solver.dy = 2.0
    
        expected_u = np.ones((5,10))*200.
        expected_u[4,2:4]=800.
    
        actual_u = self.solver.set_initial_condition()
    
>       np.testing.assert_allclose(actual_u,expected_u)
E       AssertionError: 
E       Not equal to tolerance rtol=1e-07, atol=0
E       
E       Mismatched elements: 2 / 50 (4%)
E       Max absolute difference: 600.
E       Max relative difference: 0.75
E        x: array([[200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],
E              [200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],
E              [200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],...
E        y: array([[200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],
E              [200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],
E              [200., 200., 200., 200., 200., 200., 200., 200., 200., 200.],...

tests/unit/test_diffusion2d_functions.py:70: AssertionError
============================================== short test summary info ===============================================
FAILED tests/unit/test_diffusion2d_functions.py::TestOperations::test_initialize_domain - AssertionError: 200 != 100
FAILED tests/unit/test_diffusion2d_functions.py::TestOperations::test_initialize_physical_parameters - AssertionErr...
FAILED tests/unit/test_diffusion2d_functions.py::TestOperations::test_set_initial_condition - AssertionError: 
============================================ 3 failed, 2 passed in 0.81s =============================================

## Integration test log

> python -m pytest tests/integration 
================================================ test session starts =================================================
platform linux -- Python 3.8.11, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/hornekte/Desktop/testing-python-exercise
collected 2 items                                                                                                    

tests/integration/test_diffusion2d.py FF                                                                       [100%]

====================================================== FAILURES ======================================================
________________________________________ test_initialize_physical_parameters _________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        w = 30.0
        h = 12.0
        dx = 0.3
        dy = 0.6
        d = 20.0
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d)
    
        expected_dt = approx(0.0018, abs=0.000001)
    
        actual_dt = solver.dt
    
>       assert actual_dt == expected_dt
E       assert 0.00045 == 0.0018 ± 1.0e-06

tests/integration/test_diffusion2d.py:27: AssertionError
------------------------------------------------ Captured stdout call ------------------------------------------------
dt = 0.00045
_____________________________________________ test_set_initial_condition _____________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        w = 6.0
        h = 8.0
        dx = 0.3
        dy = 0.5
        d = 20.0
        T_cold = 300.0
        T_hot = 400.0
    
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        expected_u = T_cold * np.ones((20, 16))
        expected_u[11:20, 7:14] = 400.0
        expected_u[11:13, 7] = 300.0
        expected_u[11:13, 13] = 300.0
    
        actual_u = solver.set_initial_condition()
    
>       np.testing.assert_allclose(actual_u, expected_u)
E       AssertionError: 
E       Not equal to tolerance rtol=1e-07, atol=0
E       
E       (shapes (26, 16), (20, 16) mismatch)
E        x: array([[300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,
E               300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,...
E        y: array([[300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,
E               300., 300., 300., 300., 300.],
E              [300., 300., 300., 300., 300., 300., 300., 300., 300., 300., 300.,...

tests/integration/test_diffusion2d.py:54: AssertionError
------------------------------------------------ Captured stdout call ------------------------------------------------
dt = 0.0005955882352941177
============================================== short test summary info ===============================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.00045 == 0.0018 ± 1.0e-06
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - AssertionError: 
================================================= 2 failed in 0.78s ==================================================


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
