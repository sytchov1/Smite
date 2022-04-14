import React, { useContext, useEffect, useState } from 'react'
import classes from './Tooltip.module.css'
import { WindowContext } from '../../../context';


function Tooltip(props) {
  let windowSize = useContext(WindowContext);
  const [position, setPosition] = useState({x: 0, y: 0});
  const [height, setHeight] = useState();
  const tooltip = React.createRef();

  useEffect(() => setHeight(tooltip.current.clientHeight));

  useEffect(() => {
    let x = (props.position.x + 340) >= windowSize.width ? props.position.x - 340 : props.position.x + 20
    let y = (props.position.y + height + 10) >= windowSize.height ? props.position.y - (height + 10) : props.position.y + 10
    setPosition({x: x, y: y})
  }, [windowSize, props.position])

  
  return (
    <div className={ classes.Tooltip }
      dangerouslySetInnerHTML={{ __html: props.children }}
      style={{top: position.y, left: position.x}}
      ref={tooltip}>
    </div>
  )
}

export default Tooltip