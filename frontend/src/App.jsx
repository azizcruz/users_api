import React, { Component } from 'react';
import './App.css';
import { UserComponent } from './components/UserComponent'
import axios from 'axios'

export class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      users: []
    }
  }
  componentDidMount() {
    axios.get('http://localhost:8000/users/')
      .then(users => {
        this.setState({
          users: users.data
        })
        console.log(this.state.users)
      })
      .catch(err => {
        console.log(err)
      })
  }
  render() {
    return (
      <div>
        <div className="App">
          <header className="App-header">
            {
             (this.state.users.length > 0) ?
              this.state.users.map((user, key) => {
                return <UserComponent user={user} key={key}></UserComponent>
              }) 
             : <h3>No data found</h3>
            }
          </header>
        </div>
      </div>
    )
  }
}

export default App
