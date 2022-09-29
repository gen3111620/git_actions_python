# git_actions_python
github actions practice project 


## actions yml syntax introduction

* name : workflows name (建立workflows的名稱)
* on : To automatically trigger a workflow use on to define which events can cause the workflow to run. (觸發開始run event的條件，你可定義例如當push到master時，觸發事件)
* jobs : A workflow run is made up of one or more jobs, which run in parallel by default. To run jobs sequentially, you can define dependencies on other jobs using the jobs.<job_id>.needs keyword. 是一連串的steps組成，可以擁有1至多個job
* steps : 運行命令(run)，執行actions(uses) or 設定參數
* uses : 使用github上別人開源已寫好的action
* run : 執行command
* with : 設定變數
* matrix : define a matrix of different job configurations. Within your matrix

![alt text](https://github.com/gen3111620/git_actions_python/blob/main/actions.png?raw=true)

```
jobs:
  example_matrix:
    strategy:
      matrix:
        version: [10, 12, 14]
    steps:
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.version }}
```