import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import Nav from '../common/Nav'

class Login extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, error: '', editor: '' }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmitWriter = this.handleSubmitWriter.bind(this)
    this.handleSubmitEditor = this.handleSubmitEditor.bind(this)
    this.pathCheck = this.pathCheck.bind(this)

  }

  pathCheck() {
    if(this.props.location.pathname === '/editorlogin')
      this.setState({ type: 'editor' })
    else if(this.props.location.pathname === '/writerlogin')
      this.setState({ type: 'writer' })
  }


  componentDidMount() {
    this.pathCheck()
  }

  handleChange({ target: { name, value }}) {
    const data = {...this.state.data, [name]: value }
    this.setState({ data, error: '' })
  }

  handleSubmitEditor(e) {
    e.preventDefault()

    axios.post('/api/editorlogin', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        this.props.history.push('/edit-writings')
      })
      .catch(() => this.setState({ error: 'Invalid Crendentials'}))
  }

  handleSubmitWriter(e) {
    e.preventDefault()

    axios.post('/api/login', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        this.props.history.push('/writingsubmit')
      })
      .catch(() => this.setState({ error: 'Invalid Crendentials'}))
  }



  render(){
console.log(this.state.type)
    return (

      <main>
  <Nav type={this.state.type} pathCheck={this.pathCheck}/>
        {(this.state.type === 'writer') &&
        <form className="form-style login" onSubmit={this.handleSubmitWriter}>

          <label className='label'>Email</label>
          <div className="control">
            <input
              onChange = {this.handleChange}
              className="input"
              name="email"
              placeholder="Your Email Please."/>
          </div>
          <label className='label'>Password</label>
          <div className="control">
            <input
              onChange = {this.handleChange}
              type="password"
              className="input"
              name="password"
              placeholder="Your Password Please."/>
          </div>

          <button type="submit" className="button" > Login as Writer</button>
        </form>}
        {(this.state.type === 'editor') && <form className="form-style login"  onSubmit={this.handleSubmitEditor} >

          <label className='label'>Email</label>
          <div className="control">
            <input
              onChange = {this.handleChange}
              className="input"
              name="email"
              placeholder="Your Email Please."/>
          </div>
          <label className='label'>Password</label>
          <div className="control">
            <input
              onChange = {this.handleChange}
              type="password"
              className="input"
              name="password"
              placeholder="Your Password Please."/>
          </div>
          <button type="submit" className="button"> Login as Editor</button>

        </form>}
      </main>
    )
  }
}

export default Login
