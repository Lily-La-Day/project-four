import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

import Nav from '../common/Nav'
import OwnWritingShow from './OwnWritingShow'

class WriterProfile extends React.Component {
  constructor() {
    super()
    this.state = { writer: null }
    // this.logout = this.logout.bind(this)
    // this.requestFunction = this.requestFunction.bind(this)
    // this.messagesFunction = this.messagesFunction.bind(this)
    // this.handleInterest = this.handleInterest.bind(this)
    // this.handleSubmit = this.handleSubmit.bind(this)
    // this.getData = this.getData.bind(this)
    // this.messagesFunction = this.messagesFunction.bind(this)
    // this.requestFunction = this.requestFunction.bind(this)

  }


  logout() {
    Auth.logout()
    this.props.history.push('/')
  }



  componentDidMount() {
    this.getData()
  }

  getData(){
    console.log('getting data')
    axios.get('/api/writerprofile', {
      headers: { Authorization: ` ${Auth.getToken()}` }
    })
      .then(res => this.setState({ writer: res.data }))
      .catch(() => this.setState({ error: 'Invalid Crendentials' }))
  }



  // getEvent(){
  //   axios.get('/api/event', {
  //     headers: { Authorization: ` ${Auth.getToken()}` }
  //   })
  //     .then(res => this.setState({ writer: res.data }))
  //     .catch(() => this.setState({ error: 'Invalid Crendentials' }))
  // }

  // handleInterest(e) {
  //   this.setState({ data: { interests: e.value }  })
  //     .catch(err => console.log(err))
  // }

  // handleSubmit(e) {
  //   e.preventDefault()
  //   const data = this.state.data
  //   console.log('data is', data.interests, `/api/writers/${this.state.writer._id}`)
  //   axios.put(`/api/writers/${this.state.writer._id}`, data , {
  //     headers: { 'Authorization': `${Auth.getToken()}` }
  //   })
  //     .then(() => this.getData())
  //     .catch(err => console.log(err))
  //
  // }




  render(){
    console.log(writer, 'writer profile rendering')
    if (!this.state.writer) return null
    const { writer } = this.state
    console.log(writer, 'writer profile rendering')
    return (


      <section>
        <Nav />
        <section className="profile grid-container"/>
        {writer.created_writings.map((writing, i) => (

          <div key={i} className ="writing">
            <span key={writing.id}><h3 key={writing.id}> {writing.title}</h3></span>

            <OwnWritingShow writing={writing}/>
          </div>




        ))}

      </section>


    )


  }

}


export default WriterProfile
