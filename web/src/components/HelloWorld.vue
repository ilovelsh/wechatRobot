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
        <el-main v-if="this.activeIndex2 == '1-1' || this.activeIndex2 == '1-2'">
          <el-row :gutter="20">
            <el-col :span="16">
              <div class="grid-content bg-purple">
                <el-transfer
                  filterable
                  :filter-method="filterMethod"
                  filter-placeholder="搜索"
                  :titles="['可选列表', '发送列表']"
                  v-model="value2"
                  :data="data2"
                >
                </el-transfer>
              </div>
            </el-col>
            <el-col :span="8">
              <div class="grid-content bg-purple">
                <el-radio-group v-model="orderType">
                  <el-radio :label="1">立即任务</el-radio>
                  <el-radio :label="2">定时任务</el-radio>
                  <el-radio :label="3">循环任务</el-radio>
                </el-radio-group>
                <div v-if="orderType == 2" class="selectClass">
                  任务执行时间：
                  <el-date-picker
                    v-model="value3"
                    type="datetime"
                    placeholder="选择日期时间">
                  </el-date-picker>
                </div>
                <div v-if="orderType == 3">
                  <el-row :gutter="10">
                    <el-col :span="8"><el-input v-model="input" placeholder="0-23"><template slot="append">小时</template></el-input></el-col>
                    <el-col :span="8"><el-input v-model="input" placeholder="0-59"><template slot="append">分钟</template></el-input></el-col>
                    <el-col :span="8"><el-input v-model="input" placeholder="0-59"><template slot="append">秒</template></el-input></el-col>
                  </el-row>
                </div>
                <el-radio-group v-model="msgType">
                  <el-radio :label="1">文字消息</el-radio>
                  <el-radio :label="2">语音消息</el-radio>
                </el-radio-group>
                <el-radio-group v-model="msgType">
                  <el-radio :label="3">图片消息</el-radio>
                  <el-radio :label="4">文件消息</el-radio>
                </el-radio-group>
                <div v-if="msgType == 1" class="msgClass">
                  <el-input
                    type="textarea"
                    :rows="6"
                    placeholder="请输入内容"
                    v-model="textarea">
                  </el-input>
                </div>
                <div v-if="msgType == 3" class="msgClass">
                  <el-upload
                    action="https://jsonplaceholder.typicode.com/posts/"
                    list-type="picture-card"
                    :on-preview="handlePictureCardPreview"
                    :before-upload="beforeAvatarUpload"
                    :on-remove="handleRemove">
                    <i class="el-icon-plus"></i>
                  </el-upload>
                  <el-dialog :visible.sync="dialogVisible">
                    <img width="100%" :src="dialogImageUrl" alt="">
                  </el-dialog>
                </div>
                <div v-if="msgType == 4 || msgType == 2" class="msgClass">
                  <el-upload
                    class="upload-demo"
                    drag
                    action="https://jsonplaceholder.typicode.com/posts/"
                    :before-upload="beforeAvatarUpload"
                    multiple>
                    <i class="el-icon-upload"></i>
                    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                  </el-upload>
                </div>
                <el-row>
                  <el-button type="success" round>成功按钮</el-button>
                  <el-button type="info" round>信息按钮</el-button>
                </el-row>
              </div>
            </el-col>
          </el-row>
        </el-main>
        <el-main v-else-if="this.activeIndex2 == 2">
            <el-table
              :data="tableData"
              style="width: 100%">
              <el-table-column
                prop="date"
                label="编号"
                width="180">
              </el-table-column>
              <el-table-column
                prop="orderType"
                label="任务类型"
                width="180">
              </el-table-column>
              <el-table-column
                prop="status"
                label="状态">
              </el-table-column>
            </el-table>
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
      user: null,
      data2: [],
      value1: '',
      value2: [],
      value3: '',
      activeIndex2: '1',
      orderType: 1,
      msgType: 1,
      textarea: '',
      filterMethod (query, item) {
        return item.pinyin.indexOf(query) > -1
      },
      dialogImageUrl: '',
      dialogVisible: false
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      // console.log(key, keyPath)
      this.activeIndex2 = key
    },
    handleRemove (file, fileList) {
      // console.log(file, fileList)
    },
    beforeAvatarUpload (file) {
      // 文件格式判定
      const isPic = this.isPicture(file.type)
      const isMP3 = file.type === 'mp3'
      // 文件大小判定
      const isLt2M = file.size / 1024 / 1024 < 2

      if (this.msgType === 3) {
        if (!isPic) {
          this.$message.error('上传必须是图片格式！')
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!')
        }
        return isPic && isLt2M
      } else if (this.msgType === 2) {
        if (!isMP3) {
          this.$message.error('上传必须是MP3格式！')
        }
        return isMP3
      }
    },
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    isPicture (fileType) {
      var flag = false
      if (fileType === 'image/jpeg') {
        flag = true
      } else if (fileType === 'image/png') {
        flag = true
      }
      return flag
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
  margin-bottom: 10px;
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
.grid-content {
  padding: 25px 0px;
}
.el-radio-group {
  margin: 5px 0px;
}
.msgClass {
  padding: 5px 20px;
}
.selectClass {
  padding: 5px 20px;
}
</style>
