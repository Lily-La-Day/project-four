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
    this.rate = this.rate.bind(this)



  }



  starRating(e) {
    const one = document.querySelector('.one')
    const two = document.querySelector('.two')
    const three = document.querySelector('.three')
    const four = document.querySelector('.four')
    const five = document.querySelector('.five')

    if(!this.rated)
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

    console.log(this.state.rating)
    console.log('rating')
    axios.post(`/api/edits/${this.props.edit.id}/like`, this.state,  {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}


    })
      .catch((err) => console.log(err))
    this.rated = true
    document.querySelector('.thank-you').style.display = 'block'
    document.querySelector('.rateButton').style.display = 'none'
  }







  render() {

    if (!this.props.edit) return null

    console.log(this.props.edit)
    return (
      <main>


        <h2 className="writingTitle">{this.props.edit.title}</h2>
        <h5 className="edit-snippet"> {this.props.edit.text}</h5>
        <div>
          <div className="content">
            <h3>Rate This Edit</h3>

            <div className="wrapper">
              <img src="/assets/star.svg" className="starBefore one"  onClick={this.starRating}/>
              <img src="/assets/star.svg"  className="starBefore two" onClick={this.starRating}/>
              <img src="/assets/star.svg"  className="starBefore three" onClick={this.starRating}/>
              <img src="/assets/star.svg" className="starBefore four" onClick={this.starRating}/>
              <img src="/assets/star.svg" className="starBefore five" onClick={this.starRating}/>


            </div>


          </div>


          <div className="rating-container">
            <p className='none star-text'> Click below to confirm your rating </p>
            <button className="rateButton button" onClick={this.rate} > rate </button>
            <h3 className="thank-you"> Thank you for rating! This edit currently has a rating of {this.props.edit.rating + this.state.rating}</h3>
          </div>

        </div>


      </main>


    )
  }
}

export default EditRate
