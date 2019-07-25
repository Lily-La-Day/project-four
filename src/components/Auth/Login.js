import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

class Login extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, error: '' }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmitWriter = this.handleSubmitWriter.bind(this)
    this.handleSubmitEditor = this.handleSubmitEditor.bind(this)
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
        this.props.history.push('/writings')
      })
      .catch(() => this.setState({ error: 'Invalid Crendentials'}))
  }

  handleSubmitWriter(e) {
    e.preventDefault()

    axios.post('/api/writerlogin', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        this.props.history.push('/writings')
      })
      .catch(() => this.setState({ error: 'Invalid Crendentials'}))
  }

  render(){
    return (
      <main>
        <form className="form-style login" >

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
          <button type="submit" className="button" onSubmit={this.handleSubmitEditor}> Login as Editor</button>
          <button type="submit" className="button" onSubmit={this.handleSubmitWriter}> Login as Writer</button>
        </form>
      </main>
    )
  }
}

export default Login
