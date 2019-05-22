from subprocess import *


class OS:
    def runner(self, cmd, return_result=False):
        res = ''
        try:
            if not return_result:
                Popen(cmd, shell=True)
            else:
                res = check_output(cmd, shell=True)
        except Exception as e:
            return e.args
        else:
            if return_result:
                return res.decode("utf-8")
            return 0

    def sudo(self, password, run=False):
        cmd = f"echo {password} | sudo -S "
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)

    def service(self, tool, action, run=False):
        cmd = f"service {tool} {action}"
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)

    def ls(self, path, run=True):
        cmd = "ls " + path
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)

    def pwd(self, run=True):
        cmd = "pwd"
        if not run:
            return cmd
        return self.runner(cmd, return_result=True)

    def __str__(self):
        cmd = "uname -a"
        return str(self.runner(cmd, return_result=True))

    def __call__(self, *args, **kwargs):
        cmd = "uname -a"
        return str(self.runner(cmd, return_result=True))
