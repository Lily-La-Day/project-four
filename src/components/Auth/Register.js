import React from 'react'
import axios from 'axios'

class Register extends React.Component {
  constructor() {
    super()

    this.state ={ data: {}, errors: {} }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmitWriter = this.handleSubmitWriter.bind(this)
    this.handleSubmitEditor = this.handleSubmitEditor.bind(this)
  }

  handleChange({ target: { name, value }}) {
    const data = { ...this.state.data, [name]: value }
    const errors = {...this.state.errors, [name]: ''}
    this.setState({ data, errors })
  }

  handleSubmitWriter(e) {
    e.preventDefault()
    axios.post('/api/register', this.state.data )
      .then(() => this.props.history.push('/login'))
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  handleSubmitEditor(e) {
    e.preventDefault()
    axios.post('/api/editorregister', this.state.data )
      .then(() => this.props.history.push('/login'))
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }



  render() {
    console.log(this.state)
    return (
      <main className="section">

        <section className="container">
          <form className="register form-style" >

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
            <button type="submit" onSubmit={this.handleSubmitWriter}>Sign-Up to Write</button>
            <button type="submit" onSubmit={this.handleSubmitWriter}>Sign-Up to Edit</button>
          </form>
        </section>
      </main>
    )
  }
}
export default Register
