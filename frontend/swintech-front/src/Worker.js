import React, { useState } from "react";
import axios from "axios";
import "./Worker.css";

function RestAPI() {
  const [text, setText] = useState([]);

  return (
    <>
      <h1>API 연습</h1>
      <div className="btn-primary">
        <button
          onClick={() => {
            axios
              .post("http://127.0.0.1:8000/worker/", {
                title: "직원번호_성명",
              })
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
                console.log(error);
              });
          }}
        >
          직원 추가
        </button>
        <button
          onClick={() => {
            axios
              .get("http://127.0.0.1:8000/worker/")
              .then((response) => {
                setText([...response.data]);
                console.log(response.data);
              })
              .catch(function (error) {
                console.log(error);
              });
          }}
        >
          직원목록
        </button>
      </div>
      {text.map((e) => (
        <div>
          {" "}
          <div className="list">
            <span>
              {e.wid}번, {e.workerName}
            </span>
            <button
              className="btn-delete"
              onClick={() => {
                axios.delete(`http://127.0.0.1:8000/worker/${e.wid}/`);
                setText(text.filter((text) => text.wid !== e.wid));
              }}
            >
              DELETE
            </button>{" "}
          </div>
        </div>
      ))}
    </>
  );
}

export default RestAPI;