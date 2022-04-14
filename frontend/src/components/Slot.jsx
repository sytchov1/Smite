import React, { useState } from 'react'
import '../styles/App.css'
import { ITEM_COLORS } from '../values/colors.js'
import Tooltip from './UI/tooltip/Tooltip';


function Slot(props) {
  const color = props.item ? ITEM_COLORS[props.item.quality] : '';
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
    <div className='Slot' style={{ flexDirection:  props.reverse }}>
        <div className='slot-icon' onClick={() => props.openModal(props.name, props.item)}
          onMouseEnter={handleHover} onMouseLeave={handleLeave} onMouseMove={handleMove}
          style={props.item
            ? {backgroundImage: `url(https://wow.zamimg.com/images/wow/icons/large/${props.item.icon}.jpg)`}
            : {}}>

        </div>
        <div className='slot-info' style={{color: `${color}`}}>
          {props.item
            ? props.item.name
            : props.name
          }
        </div>
        {hover && props.item &&
          <Tooltip position={cursorPosition}>{props.item.html_tooltip}</Tooltip>
        }
    </div>
  )
}

export default Slot