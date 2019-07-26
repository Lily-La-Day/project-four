import React from 'react'
import axios from 'axios'

class Register extends React.Component {
  constructor() {
    super()

    this.state ={ data: {}, errors: {}, type: '' }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmitWriter = this.handleSubmitWriter.bind(this)
    this.handleSubmitEditor = this.handleSubmitEditor.bind(this)
    this.makeChoice = this.makeChoice.bind(this)
  }

  handleChange({ target: { name, value }}) {
    const data = { ...this.state.data, [name]: value }
    const errors = {...this.state.errors, [name]: ''}
    this.setState({ data, errors })
  }

  handleSubmitWriter(e) {
    e.preventDefault()
    axios.post('/api/register', this.state.data )
      .then(() => this.props.history.push('/writerlogin'))
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  handleSubmitEditor(e) {
    e.preventDefault()
    axios.post('/api/editorregister', this.state.data )
      .then(() => this.props.history.push('/editorlogin'))
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  makeChoice(e) {

    if(e.target.classList.contains('editor')) {
      console.log(e.target.innerHTML)
      this.setState({ type: 'editor' })
    }else if(e.target.classList.contains('writer')){
      this.setState({ type: 'writer' })
    }

    document.querySelectorAll('.choice').forEach(el => el.style.display = 'none')

  }


  render() {
    console.log(this.state)
    return (
      <main className="section">

        <section className="container">
          <button className="choice writer" onClick={this.makeChoice}>Sign-Up to Write </button>  <button className="choice editor" onClick={this.makeChoice}>Sign-Up to Edit </button>
          {(this.state.type === 'writer') &&  <form className="register form-style" onSubmit={this.handleSubmitWriter} >

            <div className="field">
              {/* <label className="label">Username</label> */}
              <div className="control">
                <input
                  className="input"
                  name="username"
                  placeholder="Username"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="field">
              {/* <label className="label">Email</label> */}
              <div className="control">
                <input
                  className="input"
                  name="email"
                  placeholder="Email"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="field">
              {/* <label className="label">Password</label> */}
              <div className="control">
                <input
                  className="input"
                  type="password"
                  name="password"
                  placeholder="Password"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="field">
              {/* <label className="label">Password Confirmation</label> */}
              <div className="control">
                <input
                  className="input"
                  type="password"
                  name="password_confirmation"
                  placeholder="Password Confirmation"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <button type="submit">Sign-Up to Write </button>

          </form>}

          {(this.state.type === 'editor') && <form className="register form-style" onSubmit={this.handleSubmitEditor} >

            <div className="field">
              {/* <label className="label">Username</label> */}
              <div className="control">
                <input
                  className="input"
                  name="username"
                  placeholder="Username"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="field">
              {/* <label className="label">Email</label> */}
              <div className="control">
                <input
                  className="input"
                  name="email"
                  placeholder="Email"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="field">
              {/* <label className="label">Password</label> */}
              <div className="control">
                <input
                  className="input"
                  type="password"
                  name="password"
                  placeholder="Password"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="field">
              {/* <label className="label">Password Confirmation</label> */}
              <div className="control">
                <input
                  className="input"
                  type="password"
                  name="password_confirmation"
                  placeholder="Password Confirmation"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <button type="submit">Sign-Up to Edit </button>

          </form>}

        </section>
      </main>
    )
  }
}
export default Register
