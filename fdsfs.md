response: {
  'data': [ all info from the incident table ],
  'incident_times': [
    (incident times that match incident id, ordered by realtime, earliest first)
        {
        "inctimes_id": 20573551,
        "timedesc": 0,
        "responder_id": null,
        "realtime": "2016-10-19T09:07:06"
      },
      {
        "inctimes_id": 20573552,
        "timedesc": 1,
        "responder_id": null,
        "realtime": "2016-10-19T09:07:19"
      },...
  ],
  'responders': [
    (responders that match incident id)
       {
           "responder_id": 1,
           "responderunit": 7,
           "codetosc": 3
       },
       {
           "responder_id": 2,
           "responderunit": 8,
           "codetosc": 3
       },...
  ],
  "response_time": 280.0,
  this calculation is in seconds based on:
  a = realtime of incident_time matching timedesc of 0 (received)
  b = realtime of first incident_time matching timedesc of 5 (on scene), ordered by realtime
  (b-a).total_seconds
}
