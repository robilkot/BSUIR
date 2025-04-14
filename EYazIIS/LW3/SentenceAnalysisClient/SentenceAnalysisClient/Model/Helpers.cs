using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace SentenceAnalysisClient.Model
{
    public class HeadIdConverter : JsonConverter<string?>
    {
        public override bool CanConvert(Type objectType)
        {
            return typeof(string) == objectType;
        }

        public override string? Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            if (reader.TokenType == JsonTokenType.Number)
            {
                int value = reader.GetInt32();
                return value == -1 ? null : value.ToString();
            }

            if (reader.TokenType == JsonTokenType.String)
            {
                string strValue = reader.GetString()!;
                return strValue == "-1" ? null : strValue;
            }

            throw new JsonException($"Unsupported token type {reader.TokenType}");
        }

        public override void Write(Utf8JsonWriter writer, string? value, JsonSerializerOptions options)
        {
            if (value == null)
            {
                writer.WriteNumberValue(-1);
            }
            else
            {
                writer.WriteStringValue(value);
            }
        }
    }
}
