import React from 'react'
import classes from './Input.module.css'

const Input = React.forwardRef((props, ref) => {
    return (
        <div className={classes.InputContainer}>
            <input ref={ref} className={classes.Input} {...props} />
            <span className={classes.Underline}></span>
        </div>
    );
});

export default Input