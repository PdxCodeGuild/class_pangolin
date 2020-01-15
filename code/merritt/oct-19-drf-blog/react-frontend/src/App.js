import React, { Component } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    posts: []
  }
  componentDidMount() {
    this.getPosts();
  }
  getPosts() {
    axios
      .get("http://127.0.0.1:8000/api/v1/")
      .then(res => this.setState({posts: res.data}))
      .catch(error => console.log(error));
  }
  render() {
    return (
      <div>
        {this.state.posts.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
