# global
from hypothesis import strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_test
import ivy


# Helpers #
# ------- #


# dirichlet
@handle_test(
    fn_tree="functional.ivy.experimental.dirichlet",
    dtype_and_alpha=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("float", index=2),
        shape=st.tuples(
            st.integers(min_value=2, max_value=5),
        ),
        min_value=0,
        max_value=100,
        exclude_min=True,
    ),
    size=st.tuples(
        st.integers(min_value=2, max_value=5), st.integers(min_value=2, max_value=5)
    ),
    seed=helpers.ints(min_value=0, max_value=100),
)
def test_dirichlet(
    *,
    dtype_and_alpha,
    size,
    seed,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    dtype, alpha = dtype_and_alpha

    def call():
        return helpers.test_function(
            ground_truth_backend=ground_truth_backend,
            input_dtypes=dtype,
            test_flags=test_flags,
            test_values=False,
            fw=backend_fw,
            fn_name=fn_name,
            on_device=on_device,
            alpha=alpha[0],
            size=size,
            seed=seed,
        )

    ret, ret_gt = call()
    if seed:
        ret1, ret_gt1 = call()
        assert ivy.any(ret == ret1)
    ret = helpers.flatten_and_to_np(ret=ret)
    ret_gt = helpers.flatten_and_to_np(ret=ret_gt)
    for (u, v) in zip(ret, ret_gt):
        u, v = ivy.array(u), ivy.array(v)
        assert ivy.all(ivy.sum(u, axis=-1) == ivy.sum(v, axis=-1))
        assert ivy.all(u >= 0) and ivy.all(u <= 1)
        assert ivy.all(v >= 0) and ivy.all(v <= 1)


# beta
@handle_test(
    fn_tree="functional.ivy.experimental.beta",
    dtype_and_alpha_beta=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("float"),
        min_value=0,
        min_num_dims=1,
        max_num_dims=2,
        num_arrays=2,
        exclude_min=True,
    ),
    seed=helpers.ints(min_value=0, max_value=100),
)
def test_beta(
    *,
    dtype_and_alpha_beta,
    seed,
    num_positional_args,
    as_variable,
    with_out,
    native_array,
    container_flags,
    instance_method,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
    test_flags,
):

    dtype, alpha_beta = dtype_and_alpha_beta
    if "float16" in dtype:
        return
    ret, ret_gt = helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=dtype,
        test_flags=test_flags,
        test_values=False,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        alpha=alpha_beta[0],
        beta=alpha_beta[1],
        shape=None,
        dtype=dtype[0],
        seed=seed,
    )
    ret = helpers.flatten_and_to_np(ret=ret)
    ret_gt = helpers.flatten_and_to_np(ret=ret_gt)
    for (u, v) in zip(ret, ret_gt):
        assert ivy.all(u >= 0) and ivy.all(u <= 1)
        assert ivy.all(v >= 0) and ivy.all(v <= 1)


# gamma
@handle_test(
    fn_tree="functional.ivy.experimental.gamma",
    dtype_and_alpha_beta=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("float"),
        min_value=0,
        min_num_dims=1,
        max_num_dims=2,
        num_arrays=2,
        exclude_min=True,
    ),
    seed=helpers.ints(min_value=0, max_value=100),
)
def test_gamma(
    *,
    dtype_and_alpha_beta,
    seed,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    dtype, alpha_beta = dtype_and_alpha_beta
    if "float16" in dtype:
        return
    ret, ret_gt = helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=dtype,
        test_flags=test_flags,
        test_values=False,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        alpha=alpha_beta[0],
        beta=alpha_beta[1],
        shape=None,
        dtype=dtype[0],
        seed=seed,
    )
    ret = helpers.flatten_and_to_np(ret=ret)
    ret_gt = helpers.flatten_and_to_np(ret=ret_gt)
    for (u, v) in zip(ret, ret_gt):
        assert ivy.all(u >= 0)
        assert ivy.all(v >= 0)
