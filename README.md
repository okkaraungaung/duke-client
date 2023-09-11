# Duke Client

This is a sample JavaScript web application that you will use to implement REST APIs on your current Duke program. You will turn your Duke app into a server, and this web app expects those APIs to already be defined.

> Don't worry too much about JavaScript and the web app for now. Your task is to implement the APIs that will fill in the blanks and make the app work.

## Getting Started

To set up a server in Python, you can use [Flask](https://flask.palletsprojects.com/en/2.3.x/). Flask is a simple framework for making web apps with Python. Follow the [installation](https://flask.palletsprojects.com/en/2.3.x/installation/) and [quickstart](https://flask.palletsprojects.com/en/2.3.x/quickstart/) instructions until you can see "Hello World" in your browser.

## Submoduling the Duke Client

[Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) allow you to keep and use a Git repository as a subdirectory of your main Git repository. We will be submoduling this repository so you can use the Duke Client in your app.

In the root directory of your project, create an `assets` folder. Inside it, run the following command to submodule this repo under a `client` folder.

```bash
git submodule add https://github.com/it5503-2310/duke-client.git client/
```

> Now that you added this repo as a submodule in your repo, you can open this `README.md` in Visual Studio Code and view it as a readable document there to refer when building the APIs!

## Grab the Flask template

Inside this repo, there is a `template.py` that is a skeleton Flask app with the endpoints that you are going to build. Copy this file into your project, rename, and modify it accordingly.

## Hosting the Duke Client

This repo contains the codes that power the Duke Client web app. Don't worry about what's inside.

What we need to do is to serve these files with Flask so that you can access it in your browser. Accordingly modify your current Flask set-up with these lines.

```python
from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='assets/client')

@app.get('/')
def serve_client():
    return send_from_directory('assets/client', 'index.html')
```

This set-up assumes that the `assets` folder is in the same directory as the Python file that contains these lines. If you have a different folder path, modify the `static_folder` and `send_from_directory` arguments accordingly.

You should be able to convince yourself that these lines will serve everything inside the `assets/client` folder, and respond to GET `/` with the `index.html` inside the `assets/client` folder.

## Accessing the Duke Client

Run your Flask server as you did before. Go to your browser and now visit `http://localhost:5000`. You should see the Duke Client web app.

You'll probably get a bunch of errors in the browser and/or Python console. That's because the app expects certain APIs to already be implemented. This is your task.

## API specifications

The Duke Client web app expects the following APIs to be implemented. You can use the [Postman](https://www.postman.com/) app to test your APIs in isolation without having to worry about the web app in the process.

There are five endpoints.

| Method | Path                | Description                |
| ------ | ------------------- | -------------------------- |
| GET    | `/tasks`            | Retrieves a list of tasks. |
| POST   | `/tasks`            | Creates a new task.        |
| PATCH  | `/tasks/:id/mark`   | Marks a task as done.      |
| PATCH  | `/tasks/:id/unmark` | Marks a task as not done.  |
| DELETE | `/tasks/:id`        | Deletes a task.            |

Each endpoint is described in detail below.

### GET `/tasks`

This endpoint retrieves a list of tasks.

#### Request

May optionally include a query parameter `find` with some string `keyword` to filter the tasks. For example, `/tasks?find=book` will return all tasks that contain the word "book".

#### Response

A JSON array of objects representing the tasks. Each object specifies the following fields.

| Field        | Type    | Required               | Description                                                                  |
| ------------ | ------- | ---------------------- | ---------------------------------------------------------------------------- |
| `id`         | integer | yes                    | A unique identifier of the task.                                             |
| `done`       | boolean | yes                    | `true` if the task is marked as done. Otherwise, `false`.                    |
| `type`       | string  | yes                    | The type of the task. Has to be one of `'todo'`, `'deadline'`, or `'event'`. |
| `title`      | string  | yes                    | The title of the task.                                                       |
| `due_time`   | string  | only for `"deadline"`s | The due time of the deadline task.                                           |
| `start_time` | string  | only for `"event"`s    | The start time of the event task.                                            |
| `end_time`   | string  | only for `"event"`s    | The end time of the event task.                                              |

### POST `/tasks`

This endpoint creates a new task.

#### Request

The request body is a JSON object specifies the following fields.

| Field     | Type   | Required | Description                                                                  |
| --------- | ------ | -------- | ---------------------------------------------------------------------------- |
| `type`    | string | yes      | The type of the task. Has to be one of `'todo'`, `'deadline'`, or `'event'`. |
| `payload` | object | yes      | The data required to create the task.                                        |

The `payload` object specifies the following fields.

| Field        | Type   | Required               | Description                        |
| ------------ | ------ | ---------------------- | ---------------------------------- |
| `title`      | string | yes                    | The title of the task.             |
| `due_time`   | string | only for `"deadline"`s | The due time of the deadline task. |
| `start_time` | string | only for `"event"`s    | The start time of the event task.  |
| `end_time`   | string | only for `"event"`s    | The end time of the event task.    |

For example, the following request body creates an event with title "IT5503 Lecture" that starts on Monday at 7pm and ends at 9pm.

```json
{
  "type": "event",
  "payload": {
    "title": "IT5503 Lecture",
    "start_time": "Monday 7pm",
    "end_time": "Monday 9pm"
  }
}
```

#### Response

A JSON object that represents the newly created task. The object specifies the _object fields_ specified in the GET `/tasks` response.

If the task cannot be created due to invalid request body, the response should have [status code 400](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400).

### PATCH `/tasks/:id/mark`

This endpoint marks a task of ID `id` as done. For example, a PATCH to `/tasks/1/mark` marks the task of ID `1` as done.

#### Request

No request body is required.

#### Response

A JSON object that represents the newly updated task. The object specifies the _object fields_ specified in the GET `/tasks` response.

Needless to say, it is expected that this JSON object's `done` field is `true`.

If the task with ID `id` cannot be found, the response should have [status code 404](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404).

### PATCH `/tasks/:id/unmark`

This endpoint marks a task of ID `id` as not done. For example, a PATCH to `/tasks/1/unmark` marks the task of ID `1` as not done.

#### Request

No request body is required.

#### Response

A JSON object that represents the newly updated task. The object specifies the _object fields_ specified in the GET `/tasks` response.

Needless to say, it is expected that this JSON object's `done` field is `false`.

If the task with ID `id` cannot be found, the response should have [status code 404](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404).

### DELETE `/tasks/:id`

This endpoint deletes a task of ID `id`. For example, a DELETE to `/tasks/1` deletes the task of ID `1`.

#### Request

No request body is required.

#### Response

A JSON object that represents the deleted task. The object specifies the _object fields_ specified in the GET `/tasks` response.

After a successful DELETE, the task should no longer appear when GET `/tasks`.

If the task with ID `id` cannot be found, the response should have [status code 404](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404).
