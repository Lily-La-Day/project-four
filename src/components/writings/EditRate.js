import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
// import { Link } from 'react-router-dom'






class EditRate extends React.Component {
  constructor() {
    super()

    this.state = {  'rating': {}   }
    this.starNumber =  0
    this.finalStarNumber= 0
    this.rated = false
    this.currentEdit= 1


    this.starRating = this.starRating.bind(this)
    this.submitRate = this.submitRate.bind(this)



  }




  // componentDidMount() {
  //   const edits = []
  //
  //   axios.get(`/api/writings/${this.props.writing}/edits`)
  //
  //     .then(res => this.setState({ edits: edits.concat(res.data) }))
  //     .catch(err => console.log(err))
  // }

  starRating(e) {
    const one = document.querySelector('.one')
    const two = document.querySelector('.two')
    const three = document.querySelector('.three')
    const four = document.querySelector('.four')
    const five = document.querySelector('.five')

    if(!this.state.rated)
      if(e.target.classList.contains('one')){

        one.classList.toggle('starAfter')
        this.setState({ rating: 1 })
        // this.setState({ rated: true })
      }  else if(e.target.classList.contains('two')){

        one.classList.toggle('starAfter')
        two.classList.toggle('starAfter')
        this.setState({ rating: 2 })
        // this.setState({ rated: true })
      }  else if(e.target.classList.contains('three')){

        one.classList.toggle('starAfter')
        two.classList.toggle('starAfter')
        three.classList.toggle('starAfter')
        this.setState({ rating: 3 })
        // this.setState({ rated: true })

      }  else if(e.target.classList.contains('four')){

        one.classList.toggle('starAfter')
        two.classList.toggle('starAfter')
        three.classList.toggle('starAfter')
        four.classList.toggle('starAfter')
        this.setState({ rating: 4 })
        // this.setState({ rated: true })
      } else if(e.target.classList.contains('five')){

        one.classList.toggle('starAfter')
        two.classList.toggle('starAfter')
        three.classList.toggle('starAfter')
        four.classList.toggle('starAfter')
        five.classList.toggle('starAfter')
        this.setState({ rating: 5 })
        // this.setState({ rated: true })
      }
    console.log(this.state.rating)



    document.querySelector('p').classList.remove('none')



  }

  rate() {
    this.setState({rating: this.state.rating})
    console.log(this.state.rating)
    console.log('rating')
    axios.post(`/api/edits/${this.props.edit.id}/like`, this.state,  {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}


    })
      .catch((err) => console.log(err))
  }

  submitRate() {

    switch(this.state.rating) {
      case 1:
        this.rate()
        break
      case 2:
        this.rate()
        this.rate()
        break
      case 3:
        this.rate()
        this.rate()
        this.rate()
        break
      case 4:
        this.rate()
        this.rate()
        this.rate()
        this.rate()
        break
      case 5:
        this.rate()
        this.rate()
        this.rate()
        this.rate()
        this.rate()
        break
      default:
      // code block
    }
  }





  render() {

    if (!this.props.edit) return null

    console.log(this.props.edit)

    // this.diff('human', 'humat')


    return (
      <main>
        <div className="edit-snippet-section">

          <h2 className="writingTitle">{this.props.edit.title}</h2>
          <h5 className="edit-snippet"> {this.props.edit.text}</h5>
          <div className="content">
            <h3>Rate This Edit</h3>

            <div className="wrapper">



              <img src="/assets/star.svg" className="starBefore one"  onClick={this.starRating}/>
              <img src="/assets/star.svg"  className="starBefore two" onClick={this.starRating}/>
              <img src="/assets/star.svg"  className="starBefore three" onClick={this.starRating}/>
              <img src="/assets/star.svg" className="starBefore four" onClick={this.starRating}/>
              <img src="/assets/star.svg" className="starBefore five" onClick={this.starRating}/>

              <p className='none star-text'> Click below to confirm your rating</p>

              <button className="rateButton" onClick={this.submitRate}> rate </button>



            </div>

          </div>
        </div>















      </main>

    )
  }
}

export default EditRate
