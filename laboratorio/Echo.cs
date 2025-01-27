using System.Net;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

namespace laboratorio
{
    public class Echo
    {
        private readonly ILogger<Echo> _logger;

        public Echo(ILogger<Echo> logger)
        {
            _logger = logger;
        }

        [Function("Echo")]
        public async Task<HttpResponseData> Run([HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequestData req,
            FunctionContext executionContext)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request.");

            var response = req.CreateResponse(HttpStatusCode.OK);
            response.Headers.Add("Content-Type", "text/plain; charset=utf-8");

            using (StreamReader reader = new StreamReader(req.Body))
            {
                string name = await reader.ReadToEndAsync();
                await response.WriteStringAsync($"Hello, {name}");
            }

            return response;
        }
    }
}
