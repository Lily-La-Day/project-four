import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

import Nav from '../common/Nav'
import OwnWritingShow from './OwnWritingShow'

class WriterProfile extends React.Component {
  constructor() {
    super()
    this.state = { writer: null, finals: null, toShow: null   }
  }


  logout() {
    Auth.logout()
    this.props.history.push('/')
  }



  componentDidMount() {
    this.getData()
    this.getFinals()
  }

  filterWritings() {
    console.log('filtering')
    let active = []
    active = this.state.writings.filter(writing => writing.active === true)
    this.setState({ writings: active })

  }

  getData(){

    axios.get('/api/writerprofile', {
      headers: { Authorization: ` ${Auth.getToken()}` }
    })
      .then(res => this.setState({ writer: res.data, writings: res.data.created_writings }), )
      .catch(() => this.setState({ error: 'Invalid Crendentials' }))
  }


  getFinals() {
    axios.get('/api/finals', {
      headers: { Authorization: ` ${Auth.getToken()}` }
    })
      .then(res => this.setState({ finals: res.data }))
      .then(()=> this.filterWritings())
      .then(() => this.showFinals())
      .catch(() => this.setState({ error: 'Invalid Crendentials' }))
  }

  showFinals(){
    let toShow = []
    toShow = this.state.finals.filter(final => final.edit.original.author.id === this.state.writer.id)
    this.setState({ toShow })

  }



render(){

    if (!this.state.writer) return null
    if (!this.state.finals) return null

console.log('final', this.state.finals.map(final => final.edit.text))
console.log(this.state.writer.id)

    return (
      <section>
        <Nav />
{this.state.toShow && <h2>Your Final Drafts: </h2>}
{this.state.toShow &&  this.state.toShow.map((final, i) =>
  <section>
  <h3>{final.edit.title}</h3>

  <h4>{final.edit.text}</h4>

  <h3> Submitted by: {final.edit.editor.username}</h3>

  <h6>{final.edit.original.text}</h6>




</section>
)}




        <section/>
        {this.state.writings.map((writing, i) => (
          <OwnWritingShow writing={writing}/>
          ))}

      </section>


    )


  }

}


export default WriterProfile
