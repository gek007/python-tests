import uuid

from pydantic import BaseModel


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex}"


class Event(BaseModel):
    bucket: str
    key: str
    tenant_id: str
    source: str
    meeting_id: str
    video_item_id: str
    processing_job_id: str
    correlation_id: str


def lambda_handler(event: dict, _context) -> dict:
    bucket = event["detail"]["bucket"]["name"]
    key = event["detail"]["object"]["key"]
    tenant_id = event["detail"].get("tenantId", "tenant_default")
    source = event["detail"].get("source", "manual_upload")

    meeting_id = new_id("mtg")
    video_item_id = new_id("vid")
    processing_job_id = new_id("job")
    correlation_id = new_id("corr")

    return Event(
        bucket=bucket,
        key=key,
        tenant_id=tenant_id,
        source=source,
        meeting_id=meeting_id,
        video_item_id=video_item_id,
        processing_job_id=processing_job_id,
        correlation_id=correlation_id,
    )


example_event = {
    "detail": {
        "bucket": {"name": "my-example-bucket"},
        "object": {"key": "example/file.txt"},
        "tenantId": "tenant_12345",
        "source": "system_upload",
    }
}




def main():
    event = lambda_handler(example_event, None)
    print(event)


if __name__ == "__main__":
    main()
