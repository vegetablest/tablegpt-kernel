from ipykernel.ipkernel import Kernel


class TablegptKernel(Kernel):
    banner = "This kernel is designed to ensure that unsafe code is intercepted and filtered out before execution."

    async def do_execute(
        self,
        code,
        silent,
        store_history=True,  # noqa: FBT002
        user_expressions=None,
        allow_stdin=False,  # noqa: FBT002
        *,
        cell_meta=None,
        cell_id=None,
    ):
        return await super().do_execute(
            code,
            silent,
            store_history,
            user_expressions,
            allow_stdin,
            cell_meta=cell_meta,
            cell_id=cell_id,
        )
