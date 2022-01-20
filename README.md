# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

To create this failure log change the computation in `initialize_domain()` to `self.nx = int(h / dx)`

    =================================================================================== FAILURES ====================================================================================
    ____________________________________________________________________________ test_initialize_domain _____________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        w = 22.
        h = 3.
        dx = 0.67
        dy = 0.12
    
        solver.initialize_domain(w, h, dx, dy)
    
    >       assert 32 == solver.nx
    E       assert 32 == 4
    E        +  where 4 = <diffusion2d.SolveDiffusion2D object at 0x7fe85bf7b6a0>.nx

    tests/unit/test_diffusion2d_functions.py:27: AssertionError
    ============================================================================ short test summary info ============================================================================
    FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 32 == 4
    ========================================================================== 1 failed, 4 passed in 3.25s ==========================================================================

To create this failure log change the computation in `initialize_physical_parameters()` to `self.dt = dx2 + dy2 / (2 * self.D * (dx2 + dy2))`

    =================================================================================== FAILURES ====================================================================================
    ______________________________________________________________________ test_initialize_physical_parameters ______________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        solver.dx = 0.5
        solver.dy = 0.86
    
        d = 7.0
        solver.initialize_physical_parameters(d)
    
        actual_dt_rounded = round(solver.dt, 3)
    
    >       assert 0.013 == actual_dt_rounded
    E       assert 0.013 == 0.303

    tests/unit/test_diffusion2d_functions.py:45: AssertionError
    ----------------------------------------------------------------------------- Captured stdout call ------------------------------------------------------------------------------
    dt = 0.303383762559187
    ============================================================================ short test summary info ============================================================================
    FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.013 == 0.303
    ========================================================================== 1 failed, 4 passed in 2.07s ==========================================================================    

To create this failure log change the if-statement in `set_initial_condition()` to `if p2 > r2:`

    =================================================================================== FAILURES ====================================================================================
    __________________________________________________________________________ test_set_initial_condition ___________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        solver.T_cold = 200
        solver.T_hot = 900
    
        solver.nx = 3
        solver.ny = 3
        solver.dx = 0.4
        solver.dy = 0.5
    
        # the returned ndarray should have everywhere a value of 200., according to the function
        u = solver.set_initial_condition()
    
        expected_u = np.array([[200., 200., 200.],
                              [200., 200., 200.],
                              [200., 200., 200.]])
    
    >       assert np.testing.assert_array_equal(u, expected_u) is None
    E       AssertionError: 
    E       Arrays are not equal
    E       
    E       Mismatched elements: 9 / 9 (100%)
    E       Max absolute difference: 700.
    E       Max relative difference: 3.5
    E        x: array([[900., 900., 900.],
    E              [900., 900., 900.],
    E              [900., 900., 900.]])
    E        y: array([[200., 200., 200.],
    E              [200., 200., 200.],
    E              [200., 200., 200.]])

    tests/unit/test_diffusion2d_functions.py:69: AssertionError
    ============================================================================ short test summary info ============================================================================
    FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - AssertionError: 
    ========================================================================== 1 failed, 4 passed in 2.31s ==========================================================================

### unittest log
To create this failure log change the computation in `initialize_domain()` to `self.nx = int(h / dx)`

    =================================================================================== FAILURES ====================================================================================
    ____________________________________________________________________        TestDiffusion2D.test_initialize_domain _____________________________________________________________________

    self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 22.
        h = 3.
        dx = 0.67
        dy = 0.12
    
        self.solver.initialize_domain(w, h, dx, dy)
    
    >       self.assertEqual(32, self.solver.nx)
    E       AssertionError: 32 != 4

    tests/unit/test_diffusion2d_functions.py:30: AssertionError
    ============================================================================ short test summary info ============================================================================
    FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain - AssertionError: 32 != 4
    ========================================================================== 1 failed, 4 passed in 2.54s ==========================================================================

To create this failure log change the computation in `initialize_physical_parameters()` to `self.dt = dx2 + dy2 / (2 * self.D * (dx2 + dy2))`

    =================================================================================== FAILURES ====================================================================================
    ______________________________________________________________ TestDiffusion2D.test_initialize_physical_parameters ______________________________________________________________

    self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
    
        self.solver.dx = 0.5
        self.solver.dy = 0.86
    
        d = 7.0
        self.solver.initialize_physical_parameters(d)
    
        actual_dt_rounded = round(self.solver.dt, 3)
    
      self.assertEqual(0.013, actual_dt_rounded)
    E       AssertionError: 0.013 != 0.303

    tests/unit/test_diffusion2d_functions.py:47: AssertionError
    ----------------------------------------------------------------------------- Captured stdout call ------------------------------------------------------------------------------
    dt = 0.303383762559187
    ============================================================================ short test summary info ============================================================================
    FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters - AssertionError: 0.013 != 0.303
    ========================================================================== 1 failed, 4 passed in 2.99s ==========================================================================

To create this failure log change the if-statement in `set_initial_condition()` to `if p2 > r2:`

    =================================================================================== FAILURES ====================================================================================
    __________________________________________________________________ TestDiffusion2D.test_set_initial_condition ___________________________________________________________________

    self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
    
        self.solver.T_cold = 200
        self.solver.T_hot = 900
    
        self.solver.nx = 3
        self.solver.ny = 3
        self.solver.dx = 0.4
        self.solver.dy = 0.5
    
        # the returned ndarray should have everywhere a value of 200., according to the function
        u = self.solver.set_initial_condition()
    
        expected_u = np.array([[200., 200., 200.],
                               [200., 200., 200.],
                               [200., 200., 200.]])
    
    >       self.assertIsNone(np.testing.assert_array_equal(expected_u, u))
    E       AssertionError: 
    E       Arrays are not equal
    E       
    E       Mismatched elements: 9 / 9 (100%)
    E       Max absolute difference: 700.
    E       Max relative difference: 0.77777778
    E        x: array([[200., 200., 200.],
    E              [200., 200., 200.],
    E              [200., 200., 200.]])
    E        y: array([[900., 900., 900.],
    E              [900., 900., 900.],
    E              [900., 900., 900.]])

    tests/unit/test_diffusion2d_functions.py:70: AssertionError
    ============================================================================ short test summary info ============================================================================
    FAILED tests/unit/test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition - AssertionError: 
    ========================================================================== 1 failed, 4 passed in 2.03s ==========================================================================


### Integration test log

To create this failure log change the computation in `initialize_physical_parameters()` to `self.dt = dx2 + dy2 / (2 * self.D * (dx2 + dy2))`

    =================================================================================== FAILURES ====================================================================================
    ______________________________________________________________________ test_initialize_physical_parameters          ______________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        w = 22.
        h = 3.
        dx = 0.5
        dy = 0.86
    
        solver.initialize_domain(w, h, dx, dy)
    
        d = 7.0
        solver.initialize_physical_parameters(d)
    
        actual_dt_rounded = round(solver.dt, 3)
    
    >       assert 0.013 == actual_dt_rounded
    E       assert 0.013 == 0.303

    tests/integration/test_diffusion2d.py:30: AssertionError
    ----------------------------------------------------------------------------- Captured stdout call ------------------------------------------------------------------------------
    dt = 0.303383762559187


To create this failure log change the if-statement in `set_initial_condition()` to `if p2 > r2:`

    =================================================================================== FAILURES ====================================================================================
    __________________________________________________________________________ test_set_initial_condition ___________________________________________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        w = 9.
        h = 9.
        dx = 3.
        dy = 3.
    
        T_cold = 200.
        T_hot = 900.
    
        solver.initialize_domain(w, h, dx, dy)
    
        d = 7.0
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        u = solver.set_initial_condition()
    
        expected_u = np.array([[200., 200., 200.],
                                [200., 200., 200.],
                                [200., 200., 900.]])
    
    >       assert np.testing.assert_array_equal(u, expected_u) is None
    E       AssertionError: 
    E       Arrays are not equal
    E       
    E       Mismatched elements: 9 / 9 (100%)
    E       Max absolute difference: 700.
    E       Max relative difference: 3.5
    E        x: array([[900., 900., 900.],
    E              [900., 900., 900.],
    E              [900., 900., 200.]])
    E        y: array([[200., 200., 200.],
    E              [200., 200., 200.],
    E              [200., 200., 900.]])

    tests/integration/test_diffusion2d.py:59: AssertionError
    ----------------------------------------------------------------------------- Captured stdout call ------------------------------------------------------------------------------
    dt = 0.32142857142857145

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
