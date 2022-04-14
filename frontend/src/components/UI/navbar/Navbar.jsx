import React from 'react'
import classes from './Navbar.module.css'
import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <div className={ classes.navbar }>
        <Link to='/characters' className={ classes.nav_item }>Персонажи</Link>
        <Link to='/simulation' className={ classes.nav_item }>Симуляция</Link>
    </div>
  )
}

export default Navbar