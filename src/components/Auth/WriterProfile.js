import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

import Nav from '../common/Nav'
import OwnWritingShow from './OwnWritingShow'

class WriterProfile extends React.Component {
  constructor() {
    super()
    this.state = { writer: null }
  }


  logout() {
    Auth.logout()
    this.props.history.push('/')
  }



  componentDidMount() {
    this.getData()
  }

  getData(){

    axios.get('/api/writerprofile', {
      headers: { Authorization: ` ${Auth.getToken()}` }
    })
      .then(res => this.setState({ writer: res.data }))
      .catch(() => this.setState({ error: 'Invalid Crendentials' }))
  }


render(){
console.log(this.state.writer)
    if (!this.state.writer) return null


    return (
      <section>
        <Nav />

        <section/>
        {this.state.writer.created_writings.map((writing, i) => (
          <OwnWritingShow writing={writing}/>
          ))}

      </section>


    )


  }

}


export default WriterProfile
