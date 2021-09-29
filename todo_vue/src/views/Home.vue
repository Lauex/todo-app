<template>
<div>
  <AddTodo v-on:add-todo="addTodo"/>
  <Todos v-bind:todos="todos" v-on:markComplete="markTaskComplete" v-on:del-todo="deleteTodo"/>
</div>
</template>

<script>

import Todos from '../components/Todos';
import AddTodo from '../components/AddTodo';
import axios from 'axios';

export default {
  name: 'Home',
  components: {
    Todos,
    AddTodo
  },
  data() {
    return {
      todos: [],
    }
  },
  methods: {
    deleteTodo(id) {
        axios({
        method:'delete',
        url: 'http://127.0.0.1:8000/todos/' + id + '/',
        auth: {
            username: 'admin',
            password: 'Abcd@123'
        }
      }).then(() => {
        this.todos = this.todos.filter(todo => todo.id !== id)
      })
    },
    addTodo(newTodo) {
      axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/todos/',
          data: newTodo,
          auth: {
            username: 'admin',
            password: 'Abcd@123'
          }
      }).then(response => {
          this.todos.push(response.data)
      })
    },
    markTaskComplete(id) {
      let title = ''
      this.todos.forEach(todo => {
        if(todo.id === id) {
          title = todo.title
          todo.completed = !todo.completed
        }
      })
      axios({
        method:'put',
        url: 'http://127.0.0.1:8000/todos/' + id + '/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
          title: title,
          completed: true
        },
        auth: {
            username: 'admin',
            password: 'Abcd@123'
        }
      })
    }
  },
  created() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
        auth: {
          username: 'admin',
          password: 'Abcd@123'
        }
      }).then(response => {
        this.todos = response.data
      })
  }
}

</script>

<style>
  *{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.4;
  }

  .btn{
    display: inline-block;
    border: none;
    background: #555;
    color: #fff;
    padding: 7px 20px;
    cursor: pointer;
  }

  .btn:hover{
    background: #666;
  }

</style>
