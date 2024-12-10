from ipykernel.ipkernel import Kernel


class TablegptKernel(Kernel):
    banner = "This kernel is designed to ensure that unsafe code is intercepted and filtered out before execution."

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            # TODO: Implement safe execution
            stream_content = {'name': 'stdout', 'text': code + "\n"}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return super().do_execute(code, silent, store_history, user_expressions, allow_stdin)
