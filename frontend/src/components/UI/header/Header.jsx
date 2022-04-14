import React from 'react'
import Button from '../button/Button'
import Navbar from '../navbar/Navbar'
import classes from './Header.module.css'

function Header() {
  return (
    <div className={ classes.header }>
        <span className={ classes.logo }>SMITE</span>
        <Navbar/>
        <Button>Войти</Button>
    </div>
  )
}

export default Header