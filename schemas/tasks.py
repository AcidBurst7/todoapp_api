from pydantic import (
    BaseModel, 
    Field, 
    ConfigDict
)


class TaskSchema(BaseModel):
    text: str = Field(max_length=1000)

    model_config = ConfigDict(extra='forbid')