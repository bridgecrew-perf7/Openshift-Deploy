import React from 'react';
import useSWR from "swr";
import {NameForm} from "./NameForm";
import APIService from "./APIService";

const fetcher = (url) => fetch(url).then((res) => res.json());

export default function Hello() {
    const URL_BASE = "http://localhost:5000/api/v1/"

    const {data, error} = useSWR(
        "http://localhost:5000/api/v1/name",
        fetcher
    );

    if (error) return "An error ocurred!"
    if (!data) return "Loading..."

    console.log(data)

    const postName = (submittedName) => {
        APIService.PostData({submittedName}, `${URL_BASE}/post_name`)
    }

    const onSubmit = (event) => {
        event.preventDefault(event);
        postName(event.target.fName.value);
    }

    return (
        <div className="display-data" style={{height: "100%", width: "100%"}}>
            <NameForm onSubmit={onSubmit}/>
        </div>
    )
} 