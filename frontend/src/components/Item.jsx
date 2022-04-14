import React, { useState } from 'react'
import { ITEM_COLORS } from '../values/colors.js'
import Tooltip from './UI/tooltip/Tooltip.jsx'

function Item(props) {
  const color = ITEM_COLORS[props.item.quality];
  const [hover, setHover] = useState(false);
  const [cursorPosition, setCursorPosition] = useState({x: 0, y: 0});

  const handleHover = () => {
    setHover(true);
  }

  const handleLeave = () => {
    setHover(false);
  }

  const handleMove = (e) => {
    setCursorPosition({
      x: e.clientX,
      y: e.clientY,
    });
  }

  return (
    <div className={props.chosenItem && props.item.id === props.chosenItem.id
      ? 'item chosen'
      : 'item'}
       onClick={() => props.choseItem(props.item)}>
      <div className='item-icon' onMouseEnter={handleHover} onMouseLeave={handleLeave}
        onMouseMove={handleMove}
        style={{backgroundImage: `url(https://wow.zamimg.com/images/wow/icons/large/${props.item.icon}.jpg)`}}>
      </div>
      <div className='item-name' style={{color: `${color}`}}>{props.item.name}</div>
      {hover &&
        <Tooltip position={cursorPosition}>{props.item.html_tooltip}</Tooltip>
      }
    </div>
  )
}

export default Item