import React from 'react';
import useSWR from "swr";
import {NameForm} from "./NameForm";
import APIService from "./APIService";

const fetcher = (url) => fetch(url).then((res) => res.json());

export function Hello() {
    const URL_BASE = "http://localhost:5000/api/v1/"

    const {data, error} = useSWR(
        "http://localhost:5000/api/v1/names",
        fetcher
    );

    if (error) return "An error ocurred!"
    if (!data) return "Loading..."

    console.log(data)
    const name = data.fName

    const postName = (submittedName) => {
        APIService.PostData({submittedName}, `${URL_BASE}names`)
    }

    const onSubmit = (event) => {
        event.preventDefault(event);
        postName(event.target.fname.value);
    }

    return (
        <div className="display-data" style={{height: "100%", width: "100%", marginTop: "30px"}}>
            <NameForm onSubmit={onSubmit}/>
            <p>Last Name: {name}</p>
        </div>
    )
} 