<template>
  <div>
    <el-container>
      <el-header>
        <el-menu
          :default-active="activeIndex2"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
        >
          <el-submenu index="1">
            <template slot="title">消息中心</template>
            <el-menu-item index="1-1">发送好友消息</el-menu-item>
            <el-menu-item index="1-2">发送群聊消息</el-menu-item>
          </el-submenu>
          <el-menu-item index="2">调度中心</el-menu-item>
        </el-menu>
      </el-header>
      <el-container>
        <el-main>
          <el-row>
            <el-col :span="14">
              <div class="grid-content bg-purple">
                <el-transfer
                  filterable
                  :filter-method="filterMethod"
                  filter-placeholder="关键字进行搜索"
                  v-model="value2"
                  :data="data2">
                  <el-button class="transfer-footer" slot="left-footer" size="small">刷新</el-button>
                </el-transfer>
              </div>
            </el-col>
            <el-col :span="10">
              <div class="grid-content bg-purple-light">
                 <el-col :span="24">
                  <el-radio-group v-model="radio2">
                    <el-radio :label="3">立即任务</el-radio>
                    <el-radio :label="6">循环任务</el-radio>
                    <el-radio :label="9">定时任务</el-radio>
                  </el-radio-group>
                 </el-col>
                 <el-col :span="24">
                  <el-radio-group v-model="radio3">
                    <el-radio :label="3">文字</el-radio>
                    <el-radio :label="6">语音</el-radio>
                    <el-radio :label="8">图片</el-radio>
                    <el-radio :label="9">文件</el-radio>
                  </el-radio-group>
                 </el-col>
                 <el-col :span="24">
                   <el-input
                    type="textarea"
                    :rows="2"
                    placeholder="请输入内容"
                    v-model="textarea">
                   </el-input>
                 </el-col>
                 <el-row :gutter="20">
                  <el-col :span="12" :offset="12">
                    <el-button>确定</el-button>
                    <el-button>取消</el-button>
                  </el-col>
                </el-row>
              </div>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      activeIndex2: '1',
      radio2: 3,
      radio3: 3,
      textarea: ''
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
  padding: 0px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  margin-top: 20px;
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.transfer-footer {
  margin-left: 20px;
  padding: 6px 5px;
}
</style>
