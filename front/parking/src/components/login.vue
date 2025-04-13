<template>
    <div class="login-container">
      <h1>Login</h1>

      <form @submit.prevent="login">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" name="username" v-model="user_info.username" required>
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" name="password" v-model="user_info.password" required>
        </div>

        <button>Login</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import { useToast } from 'vue-toastification'

  const toast = useToast()

  export default {
    name: 'Login',
    data() {
      return {
        user_info: {
          username: null,
          password: null,
        }
    }
    },
    methods: {
      login() {
        console.log('Login data:', this.user_info)
        axios.post('http://localhost:8000/api/login', this.user_info)
        .then(response => {
                  toast.success('Welcome back ' + this.user_info.username + '!')
                  this.$router.push('/')
              })
              .catch(error => {
                  toast.error('Error logging in' + error.response.data.message)
              })
        }
      },
  }
  </script>

<style scoped>

h1 {
    color:#7D7D7D;
    font-size: 2em;
    font-weight: bolder;
    font-family: 'Lato';
    margin-bottom: 5%;
}

.login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    font-family: 'Lato';
    color: #7D7D7D;
}

.form-group input,
.form-group select {
    width: 200px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

button {
    padding: 10px 20px;
    background-color: #FD8074;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    align-self: center;
}

</style>