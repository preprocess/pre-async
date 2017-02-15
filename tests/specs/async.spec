--DESCRIPTION--

Test async macro

--GIVEN--

async function read($path) {
    $content = yield \Amp\File\get($path);
    return $content;
}

$async = async function($path) {
    $content = yield \Amp\File\get($path);
    return $content;
};

--EXPECT--

function read($path)
{
    return call_user_func(function ($context·0) {
        $generator·0 = function () use ($context·0) {
            extract($context·0);

            $content = yield \Amp\File\get($path);
            return $content;
        };

        return new \Amp\Coroutine($generator·0());
    }, get_defined_vars());
}

$async = function ($path) {
    return call_user_func(function ($context·1) {
        $generator·1 = function () use ($context·1) {
            extract($context·1);

            $content = yield \Amp\File\get($path);
            return $content;
        };

        return new \Amp\Coroutine($generator·1());
    }, get_defined_vars());
};
