import React, { Component } from 'react'

export class UserComponent extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-header">
                    <h1>{this.props.user.username}</h1>
                </div>
                <div className="card-body">
                    <div className="card-title">
                        <h3>Address</h3>
                    </div>
                    <div className="card-content">
                        <p>{this.props.user.address.city}</p>
                        <p>{this.props.user.address.street}</p>
                        <p>{this.props.user.address.zipcode}</p>
                        <div className="card-separator"></div>
                        <h3>Company</h3>
                        <p>{this.props.user.company[0].name}</p>
                    </div>
                </div>
            </div>
        )
    }
}

export default UserComponent
