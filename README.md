# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

=========================================================================================================== FAILURES =========================================================================================================== 
____________________________________________________________________________________________________ test_initialize_domain ____________________________________________________________________________________________________ 

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(20.,30.,0.01,0.01)
        expected_nx = 2000
        expected_ny = 3000
>       assert expected_nx == solver.nx
E       assert 2000 == 3000
E        +  where 3000 = <diffusion2d.SolveDiffusion2D object at 0x0000021D4B880548>.nx

tests\unit\test_diffusion2d_functions.py:22: AssertionError
_____________________________________________________________________________________________ test_initialize_physical_parameters ______________________________________________________________________________________________ 

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 0.1
        solver.dy = 0.2
        solver.initialize_physical_parameters(5.,200.,800.)
        expected_dt = 0.0008000000000000001
>       assert math.isclose(expected_dt,solver.dt)
E       assert False
E        +  where False = <built-in function isclose>(0.0008000000000000001, 0.0013333333333333337)
E        +    where <built-in function isclose> = math.isclose
E        +    and   0.0013333333333333337 = <diffusion2d.SolveDiffusion2D object at 0x000001B1CED3C388>.dt

tests\unit\test_diffusion2d_functions.py:35: AssertionError
----------------------------------------------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------------------------------------------- 
dt = 0.0013333333333333337
__________________________________________________________________________________________________ test_set_initial_condition __________________________________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.w = 0.1
        solver.h = 0.1
        solver.T_cold = 200.
        solver.T_hot = 800.
        solver.dx = 0.1
        solver.dy = 0.2
        solver.nx = 1
        solver.ny = 1

        # Expected result
        expected = np.array([[200.]])

        result = solver.set_initial_condition()
>       np.testing.assert_array_equal(result, expected)
E       AssertionError: 
E       Arrays are not equal
E       
E       Mismatched elements: 1 / 1 (100%)
E       Max absolute difference: 600.
E       Max relative difference: 3.
E        x: array([[800.]])
E        y: array([[200.]])

tests\unit\test_diffusion2d_functions.py:56: AssertionError
=================================================================================================== short test summary info ==================================================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 2000 == 3000
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert False
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - AssertionError:


### unittest log

=========================================================================================================== FAILURES ===========================================================================================================
____________________________________________________________________________________________ TestDiffusion2D.test_initialize_domain ____________________________________________________________________________________________ 

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(20.,30.,0.01,0.01)
        expected_nx = 2000
        expected_ny = 3000
>       self.assertEqual(expected_nx,self.solver.nx)
E       AssertionError: 2000 != 3000

tests\unit\test_diffusion2d_functions.py:28: AssertionError
_____________________________________________________________________________________ TestDiffusion2D.test_initialize_physical_parameters ______________________________________________________________________________________

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 0.1
        self.solver.dy = 0.2
        self.solver.initialize_physical_parameters(5.,200.,800.)
        expected_dt = 0.0008000000000000001
>       self.assertAlmostEqual(self.solver.dt, expected_dt)
E       AssertionError: 0.0013333333333333337 != 0.0008000000000000001 within 7 places (0.0005333333333333336 difference)

tests\unit\test_diffusion2d_functions.py:41: AssertionError
----------------------------------------------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------------------------------------------- 
dt = 0.0013333333333333337
__________________________________________________________________________________________ TestDiffusion2D.test_set_initial_condition __________________________________________________________________________________________ 

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.w = 0.1
        self.solver.h = 0.1
        self.solver.T_cold = 200.
        self.solver.T_hot = 800.
        self.solver.dx = 0.1
        self.solver.dy = 0.2
        self.solver.nx = 1
        self.solver.ny = 1

        # Expected result
        expected = np.array([[200.]])

        result = self.solver.set_initial_condition()
>       self.assertIsNone(np.testing.assert_array_equal(result, expected))
E       AssertionError: 
E       Arrays are not equal
E       
E       Mismatched elements: 1 / 1 (100%)
E       Max absolute difference: 600.
E       Max relative difference: 3.
E        x: array([[800.]])
E        y: array([[200.]])

tests\unit\test_diffusion2d_functions.py:60: AssertionError
=================================================================================================== short test summary info ==================================================================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain - AssertionError: 2000 != 3000
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters - AssertionError: 0.0013333333333333337 != 0.0008000000000000001 within 7 places (0.0005333333333333336 difference)        
FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition - AssertionError:

### integration log

===================================================================================================== test session starts ======================================================================================================
platform win32 -- Python 3.7.8, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: D:\SSE\testing-python-exercise\tests\integration
collected 2 items

test_diffusion2d.py FF                                                                                                                                                                                                    [100%]

=========================================================================================================== FAILURES =========================================================================================================== 
_____________________________________________________________________________________________ test_initialize_physical_parameters ______________________________________________________________________________________________ 

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(20.,40.,1.,10.)
        solver.initialize_physical_parameters(5.,200.,800.)
        expected_dt = 0.09900990099009900
>       assert math.isclose(solver.dt, expected_dt)
E       assert False
E        +  where False = <built-in function isclose>(9.900990099009901, 0.099009900990099)
E        +    where <built-in function isclose> = math.isclose
E        +    and   9.900990099009901 = <diffusion2d.SolveDiffusion2D object at 0x000001A7033E73C8>.dt

test_diffusion2d.py:21: AssertionError
----------------------------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------------------------
dt = 9.900990099009901
__________________________________________________________________________________________________ test_set_initial_condition __________________________________________________________________________________________________ 

    def test_set_initial_condition():
            """
            Checks function SolveDiffusion2D.get_initial_function
            """
            solver = SolveDiffusion2D()
            solver.initialize_domain(20.,40.,10.,40.)
            solver.initialize_physical_parameters(5.,200.,800.)
    
            # Expected result
            expected = np.array([[200.],[200.]])
            result = solver.set_initial_condition()
>           np.testing.assert_array_equal(result, expected)
E           AssertionError: 
E           Arrays are not equal
E
E           Mismatched elements: 2 / 2 (100%)
E           Max absolute difference: 600.
E           Max relative difference: 3.
E            x: array([[800.],
E                  [800.]])
E            y: array([[200.],
E                  [200.]])

test_diffusion2d.py:35: AssertionError
----------------------------------------------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------------------------------------------- 
dt = 150.58823529411765
=================================================================================================== short test summary info ==================================================================================================== 
FAILED test_diffusion2d.py::test_initialize_physical_parameters - assert False
FAILED test_diffusion2d.py::test_set_initial_condition - AssertionError:

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
