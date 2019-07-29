import React from 'react'
import axios from 'axios'






class FinalShow extends React.Component {
  constructor() {
    super()

    this.state = { final: null }



  }






  componentDidMount() {

    axios.get(`/api/final/${this.props.edit.id}`)
      .then(res => this.setState({ final: res.data }))
      .catch(err => console.log(err))

  }




  render() {
  
    if (!this.state.final) return null

    return (

      <main>
        <div className="writingcontainer">
<h1>The Final Version</h1>
          <h2 className="writingTitle">{this.state.final.title}</h2>

          <p> {this.state.final.text}</p>

          {/* <p> Edit submitted by: {this.state.final.edit.editor.username}</p> */}




        </div>


      </main>

    )
  }
}

export default FinalShow
