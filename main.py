from pyflowlauncher import Plugin, Result, Method
from pyflowlauncher.result import ResultResponse

plugin = Plugin()


class Query(Method):

    def __call__(self, query: str) -> ResultResponse:
        r = Result(
            Title="This is a title!",
            SubTitle="This is the subtitle!"
        )
        self.add_result(r)
        return self.return_results()

plugin.add_method(Query())
plugin.run()